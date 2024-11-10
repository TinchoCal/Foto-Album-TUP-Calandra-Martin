from flask import render_template, request, redirect, url_for, flash
from photo_album.app import app, db
from photo_album.models import Photo
from photo_album.forms import PhotoForm
import base64

@app.route('/add', methods=['GET', 'POST'])
def add_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        # Leer el archivo de imagen
        image_file = form.image.data
        image_data = base64.b64encode(image_file.read()).decode('utf-8')  # Convertir a base64

        new_photo = Photo(title=form.title.data, description=form.description.data, image=image_data)
        db.session.add(new_photo)
        db.session.commit()
        flash('Photo added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('photo_form.html', form=form)