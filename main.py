from website import create_app


# running flask application, starting the web server
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)