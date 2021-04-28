from KDA import create_app

app = create_app()


if __name__ == '__main__': #never change this "always main"
    app.run(host='0.0.0.0', port=8000, debug=True)
