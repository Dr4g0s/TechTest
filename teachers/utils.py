import csv, io, os
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.base import File


def read_profile_picture(image):
    image_path = os.path.join(settings.BASE_DIR, 'teachers_pictures', image)
    try:
        f = open(image_path, 'rb')
        return File(f)
    except Exception as e:
        raise ValidationError(e)


def read_csv_bulk(file_path):
    from teachers.models import Teacher
    try:
        csv_file = io.TextIOWrapper(file_path)
        dialect = csv.Sniffer().sniff(csv_file.read(1024), delimiters=";,")
        csv_file.seek(0)
        reader = csv.reader(csv_file, dialect)
        line_count = 0
        columns = ['First Name', 'Last Name', 'Profile picture', 'Email Address', 
                                    'Phone Number', 'Room Number', 'Subjects taught']
        for row in reader:
            if line_count == 0:
                if row != columns:
                    raise ValidationError("Columns doesn't match teacher database table!")
            else:
                if row[0] or row[1]:
                    for i in row:
                        if i == 'Â' or i == 'Â\xa0' or not i:
                            row[row.index(i)] = ''
                    obj = Teacher.objects.create(
                        first_name = row[0],
                        last_name = row[1],
                        email = row[3],
                        phone_number = row[4],
                        room_number = row[5],
                        subjects_taught = row[6],
                    )
                    if row[2] != 'Â' and row[2] != 'Â\xa0' and row[2]:
                        obj.profile_picture.save(row[2], read_profile_picture(row[2]))
                    obj.save()
            line_count += 1
    except Exception as e:
        raise ValidationError(e)
   