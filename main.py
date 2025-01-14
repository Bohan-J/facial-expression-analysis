import argparse
import save_data
import train_models
from models.dcnn_model import CustomizedCNNModel
from models.CNN_by_parts import CNNByParts


parser = argparse.ArgumentParser(description='Main program of Facial Expression Analysis')

parser.add_argument("-save_data", help="Save one of the datasets from fer2013, ck_plus, hog_bipart, and fer2013_bipart")
parser.add_argument("-train_model", help="Train one of the models from bipart_cnn or dcnn_fer13")
parser.add_argument("-test_model", help="Test one of the models from bipart_fer13, bipart_ck, dcnn_fer13")


args = parser.parse_args()

if args.save_data:
    option = args.save_data
    if option == 'fer2013':
        save_data.save_fer2013()
    elif option == 'ck_plus':
        save_data.save_ck_plus()
    elif option == 'hog_bipart':
        save_data.save_hog_bipart()
    elif option == 'fer2013_bipart':
        save_data.save_fer2013_bipart()
elif args.train_model:
    option = args.train_model
    if option == 'bipart_cnn':
        train_models.train_bipart_cnn()
    elif option == 'dcnn_fer13':
        train_models.train_dcnn_fer()
elif args.test_model:
    option = args.test_model
    if option == 'bipart_fer13':
        train_models.test('model_data/cnn_by_parts_fer13.pt')
    elif option == 'dcnn_fer13':
        train_models.test('model_data/cnn_fer2013.pt')
    elif option == 'bipart_ck+':
        train_models.test('model_data/cnn_by_parts_CK+.pt')
else:
    print('No argument found!')

