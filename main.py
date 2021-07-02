import qrcode
from csv import DictReader

all_file_paths = [["./fv_csv_files/master.csv", "./fv_png_files/"], ["./cs_csv_files/master.csv", "./cs_png_files/"]]

for file_path in all_file_paths:
    with open(file_path[0], 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=4)
            qr.add_data(row)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_path[1] + row['Computer Name'] +'.png')