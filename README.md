# Backend

There are 2 options for back-end:

 - Flask Rest API with SQLAlchemy
 - Apidogs created by origamid
	 
 You can choose between them on frontend/api.js, just comment or uncomment the desired line (first one is the apidogs and the second is the flask).

## Flask Rest API
This one is **under develop** and only have the register backend with a simple jwt authentication working

If you choose to run the Flask API here is the steps:

 1.  Create a python3.6 virtual enviroment on backend folder
 2.  Execute 'venv_name'/bin/python3.6 -m pip install -r requirements.txt
 3. To create de DB Run on virtual enviroment:  python3.6
 4. Them: `from app import db`
 5. After number 4: `db.create_all()` , now you have the sqlite db created
 6. To run the backend just go to your venv and execute the run.py
 
 If you wanna check the initial db project you can use PlantUML to view the file backend/db_model.wsd

## Dogs API

For the **full experience** use this backe-nd. For it, you just need to comment the second line on /frontend/src/api.js

# Front-end

The front-end was created with React.js and Hooks

To run just use the `npm start` on frontend folder




