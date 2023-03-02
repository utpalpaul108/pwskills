from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import os
import logging
import pymongo

logging.basicConfig(filename="image_scraping_log.log", filemode="a", format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/search-image', methods=["POST"])
def search_img():
    if request.method == "POST":
        try:
            # Create image directory to save the image
            save_img = "images/"
            if not os.path.exists(save_img):
                os.makedirs(save_img)

            query = request.form.get('search_query')
            search_query = query.replace(" ", "+")
            search_url = f"https://www.google.com/search?q={search_query}&sxsrf=AJOqlzXxMs9UlWzdFZrOcMGGgMQTnUm3fw:1677605397224&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjnh5mO37j9AhWn3HMBHeNZB5AQ_AUoAnoECAEQBA&biw=1280&bih=569&dpr=1.5"

            response = requests.get(search_url)
            soup = BeautifulSoup(response.content, "html.parser")

            image_list = soup.find_all("img")
            del image_list[0]

            all_image_data = []

            for image in image_list:
                img_url = image["src"]
                img_data = requests.get(img_url).content
                img_path = os.path.join(save_img, f"{query}_{image_list.index(image)}.jpg")
                f = open(img_path, "wb")
                f.write(img_data)
                all_image_data.append({"url": img_url, "img_data": img_data})

            client = pymongo.MongoClient(
                "mongodb+srv://utpal108:utpal123@cluster0.ipcemmi.mongodb.net/?retryWrites=true&w=majority")
            db = client['image_scraping']
            db_collection = db['images']
            db_collection.insert_many(all_image_data)

            return "Image Loaded Successfully"

        except Exception as e:
            logging.error(e)
            return "Something Went Wrong"

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
