from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return '''
    <html>
        <head>
            <style>
                body {
                    background-image: url('/static/University-of-Illinois-Zoom-background-1-3.jpg');
                    background-size: cover;
                    text-align: center;
                    padding: 50px;
                    margin: 100px;
                    backdrop-filter: blur(15px);
                    background-clip: padding-box
                }

                p {
                    margin: 10px 0;  /* Adjust top and bottom margins */
                    margin-right: 200px;
                    margin-left: 200px;
                    margin-bottom: 20px;
                    margin-top: 50px;
                }
                img {
                    width: 150px;  /* Adjust the width as needed */
                    height: 150px; /* Adjust the height as needed */
                    margin-right: 0px;  /* Add margin below the image */
                    margin-bottom: 20px;
                }
                a {
                    text-decoration: none;
                    padding: 10px 20px;
                    margin: 5px;
                    border: 2px solid #3498db;  /* Adjust the border color as needed */
                    border-radius: 5px;
                    color: #3498db;  /* Adjust the text color as needed */
                    font-weight: bold;
                    display: inline-block;
                    margin-top: 50px;
                }

                a:hover {
                    background-color: #3498db;  /* Adjust the background color on hover as needed */
                    color: #ffffff;  /* Adjust the text color on hover as needed */
                }
            </style>
        </head>
        <body>
            <img src="static/HS.png" alt="Your Image"> 
            <h1>Nakul Jain</h1>
            <p>About Me: I am currently a Senior at The University of Illinois - Urbana Champaign and will be graduating in 2024. Solving problems and brainstorming new ideas are some of the things which I relish. Besides coding, I enjoy playing my guitar and playing Badminton.</p>
            <a href="/projects">Projects</a> 
            <a href="/cv">CV</a> 
            <a href="https://www.linkedin.com/in/nakul-jain-4621651a7/">LinkedIn</a>
            <a href="https://github.com/nakulj2">GitHub</a>
            <a href="/contactinfo">Contact Info</a>
        </body>
    </html>
    '''

@app.route('/projects')
def projects():
    return '''
            <html>
                <head>
                    <style>
                        body {
                            background-image: url('/static/University-of-Illinois-Zoom-background-1-3.jpg');
                            background-size: cover;
                            text-align: center;
                            padding: 50px;
                            margin: 100px;
                            backdrop-filter: blur(15px);
                            background-clip: padding-box;
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                        }

                        .project-container {
                            display: flex;
                            flex-direction: row;
                            justify-content: space-around;
                            margin-top: 20px; /* Adjust the margin as needed */
                        }

                        .project {
                            text-align: center;
                            margin: 20px;
                        }

                        img {
                            width: 100px;  /* Adjust the width as needed */
                            height: 100px; /* Adjust the height as needed */
                            margin-bottom: 10px; /* Add margin below the image */
                        }

                        p {
                            margin: 10px 0;  /* Adjust top and bottom margins */
                        }

                        a {
                            text-decoration: none;
                            padding: 10px 20px;
                            margin: 5px;
                            border: 2px solid #3498db;  /* Adjust the border color as needed */
                            border-radius: 5px;
                            color: #3498db;  /* Adjust the text color as needed */
                            font-weight: bold;
                            display: inline-block;
                        }

                        a:hover {
                            background-color: #3498db;  /* Adjust the background color on hover as needed */
                            color: #ffffff;  /* Adjust the text color on hover as needed */
                        }
                    </style>
                </head>
                <body>
                    <div class="project-container">
                        <div class="project">
                            <img src="static/fingerprint.jpeg" alt="Your Image"> 
                            <p> fingerprint: Lorem ipsum dolor sit amet...</p>
                            <a href="https://github.com/nakulj2/FingerPrintRecognition">Finger-Print Recognition</a>
                        </div>

                        <div class="project">
                            <img src="static/handwriting_recognition.jpeg" alt="Your Image"> 
                            <p> Handwriting recognition: Lorem ipsum dolor sit amet...</p>
                            <a href="https://github.com/nakulj2/HandwritingRecognition">Handwriting Recognition</a>
                        </div>

                        <div class="project">
                            <img src="static/watchful-eye-la.jpeg" alt="Your Image"> 
                            <p> 411- project: Lorem ipsum dolor sit amet...</p>
                            <a href="https://github.com/nakulj2/WatchfulEyeLA">Watchful Eye LA</a>
                        </div>

                        <div class="project">
                            <img src="static/eda.jpeg" alt="Your Image"> 
                            <p> athlete data analysis: Lorem ipsum dolor sit amet...</p>
                            <a href="https://github.com/nakulj2/Athlete-Data-Analysis">EDA</a>
                        </div>
                    </div>
                    <a href="/">Home</a> 
                </body>
            </html>

            '''

@app.route('/cv')
def cv():
    return '''
            <html>
                <head>
                    <style>
                        body {
                            background-image: url('/static/University-of-Illinois-Zoom-background-1-3.jpg');
                            background-size: cover;
                            text-align: center;
                            padding: 50px;
                            margin: 100px;
                            backdrop-filter: blur(15px);
                            background-clip: padding-box
                        }

                        p {
                            margin: 10px 0;  /* Adjust top and bottom margins */
                            margin-right: 200px;
                            margin-left: 200px;
                            margin-bottom: 20px;
                            margin-top: 50px;
                        }
                        img {
                            width: 500px;  /* Adjust the width as needed */
                            height: 500px; /* Adjust the height as needed */
                            margin-right: 0px;  /* Add margin below the image */
                            margin-left: 100px
                            margin-bottom: 100px;
                        }
                        a {
                            text-decoration: none;
                            padding: 10px 20px;
                            margin: 5px;
                            border: 2px solid #3498db;  /* Adjust the border color as needed */
                            border-radius: 5px;
                            color: #3498db;  /* Adjust the text color as needed */
                            font-weight: bold;
                            display: inline-block;
                            margin-top: 100px;
                        }

                        a:hover {
                            background-color: #3498db;  /* Adjust the background color on hover as needed */
                            color: #ffffff;  /* Adjust the text color on hover as needed */
                        }
                    </style>
                </head>
                <body>
                    <img src="static/CV.png" alt="Your Image">
                    <a href="/">Home</a> 
                </body>
            </html>
            '''
@app.route('/contactinfo')
def contact_info():
    return '''
            <html>
                <head>
                    <style>
                        body {
                            background-image: url('/static/University-of-Illinois-Zoom-background-1-3.jpg');
                            background-size: cover;
                            text-align: center;
                            padding: 50px;
                            margin: 100px;
                            backdrop-filter: blur(15px);
                            background-clip: padding-box
                        }

                        p {
                            margin: 10px 0;  /* Adjust top and bottom margins */
                            margin-right: 200px;
                            margin-left: 200px;
                            margin-bottom: 20px;
                            margin-top: 50px;
                        }
                        img {
                            width: 500px;  /* Adjust the width as needed */
                            height: 500px; /* Adjust the height as needed */
                            margin-right: 0px;  /* Add margin below the image */
                            margin-left: 100px
                            margin-bottom: 100px;
                        }
                        a {
                            text-decoration: none;
                            padding: 10px 20px;
                            margin: 5px;
                            border: 2px solid #3498db;  /* Adjust the border color as needed */
                            border-radius: 5px;
                            color: #3498db;  /* Adjust the text color as needed */
                            font-weight: bold;
                            display: inline-block;
                            margin-top: 100px;
                        }

                        a:hover {
                            background-color: #3498db;  /* Adjust the background color on hover as needed */
                            color: #ffffff;  /* Adjust the text color on hover as needed */
                        }
                    </style>
                </head>
                <body>
                    <a href="/">Home</a> 
                </body>
            </html>
            '''

if __name__ == '__main__':
    app.run(debug=True)