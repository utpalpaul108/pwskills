from flask import Flask, render_template, request, redirect, url_for
from flask_cors import cross_origin

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging, pymongo

logging.basicConfig(filename="error_log.log", filemode="a", format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

app = Flask(__name__)


@app.route('/home')
@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/search', methods=["POST"])
@cross_origin()
def search():
    if request.method == "POST":
        chanel_name = request.form.get('chanel_name')
        chanel_url = "https://www.youtube.com/@{}/videos".format(chanel_name)
        driver_service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(chanel_url)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        # GET First Five Video URL
        video_urls = soup.find_all('a', {"class": "yt-simple-endpoint inline-block style-scope ytd-thumbnail"})[1:6]

        all_video_urls = []

        for video_url in video_urls:
            url = ""
            try:
                url = "https://www.youtube.com" + video_url["href"]
            except Exception as e:
                logging.error(e)
            finally:
                all_video_urls.append(url)

        # GET First Five Video Thumbnails
        video_thumbnails = soup.find_all('a', {"class": "yt-simple-endpoint inline-block style-scope ytd-thumbnail"})[
                           1:6]

        all_video_thumbnails = []
        for video_thumbnail in video_thumbnails:
            img_url = ""
            try:
                img_url = video_thumbnail.img["src"]
            except Exception as e:
                logging.error(e)
            finally:
                all_video_thumbnails.append(img_url)

        # GET First Five Video Titles
        video_titles = soup.find_all('a',
                                     {"class": "yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media"})[
                       1:6]

        all_video_titles = []

        for video_title in video_titles:
            title = ""
            try:
                title = video_title.text
            except Exception as e:
                logging.error(e)
            finally:
                all_video_titles.append(title)

        # GET Number of Views of the First Five Videos.
        video_views = soup.find_all('div', {"id": "metadata-line", "class": "style-scope ytd-video-meta-block"})[1:6]

        all_video_views = []

        for video_view in video_views:
            view = ""
            try:
                view = video_view.span.text
            except Exception as e:
                logging.error(e)
            finally:
                all_video_views.append(view)

        # GET the First Five Videos time of posting
        video_view_times = soup.select("div span:nth-of-type(2)", {"id": "metadata-line"})[4:9]

        all_video_view_times = []

        for video_view_time in video_view_times:
            view_time = ""
            try:
                view_time = video_view_time.text
            except Exception as e:
                logging.error(e)
            finally:
                all_video_view_times.append(view_time)

        client = pymongo.MongoClient(
            "mongodb+srv://utpal108:utpal123@cluster0.ipcemmi.mongodb.net/?retryWrites=true&w=majority")
        db = client['youtube_web_scrapping']
        db_collection = db['videos']
        db_collection.insert_one(
            {"channel_name":chanel_name, "video_urls": all_video_urls, "video_thumbnails": all_video_thumbnails, "video_titles": all_video_titles,
             "video_views": all_video_views, "video_view_times": all_video_view_times})

        return redirect(url_for('search_result'))


@app.route('/search-result')
@cross_origin()
def search_result():
    client = pymongo.MongoClient(
        "mongodb+srv://utpal108:utpal123@cluster0.ipcemmi.mongodb.net/?retryWrites=true&w=majority")
    db = client['youtube_web_scrapping']
    db_collection = db['videos']
    videos = db_collection.find()
    return render_template('search_result.html', videos=videos)


if __name__ == "__main__":
    app.run(debug=True)
