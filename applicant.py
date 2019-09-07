
from flask_restful import Resource, reqparse
import werkzeug
from PIL import Image
from flask import send_file
import uuid

class Applicant(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('image',
                       type=werkzeug.datastructures.FileStorage,
                       location='files',
                       action='append',
                       help="No image!")
    def post(self):
        
        data = Applicant.parser.parse_args()        
        images = data['image']
        
        for im in images:
            filename = str(uuid.uuid4())
            path = "./images/"+filename+".png"
            im.save(path)
        
        return {"message": "Successfull."}, 201

class Images(Resource):
    
    def get(self):
        
        return send_file("./images/1.png", mimetype="image/png")

		#ext=name.split(".")[-1]
		#mimeType='image/'+ext
		#imagePath=UPLOAD_FOLDER+"\\"+name

#		if os.path.exists(imagePath):
#			returnedImage=send_file(imagePath, mimetype=mimeType)
#			return returnedImage
#		else:
#			return {'message':'resource not found'},404
     
#    def get(self):
#        
#        im = Image.open('./images/a.png')
#        #im.show()
#    
#        return im
