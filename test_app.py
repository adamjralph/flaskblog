from pathlib import Path
import flaskblog

def test_index():
    tester = flaskblog.app.test_client()
    response = tester.get("/home", content_type="html/text")

    #assert response.status_code == 200
    #assert Path("templates/home.html")
    