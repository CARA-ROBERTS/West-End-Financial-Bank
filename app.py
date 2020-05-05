'''
Houston Flask App
Author: Andrew McKinney
Creation Date: 2020-02-14
'''

# Import Dependencies
from flask import Flask, render_template
from models import credit_crunch, approval_check
from data_packs import field_list, general_field_list, packed_field_list, basic_model_field_list, form_dict, unpacking, merge_dict
from tensorflow import keras

### DEV TOOLS ###
dev_mode = False


# Flask App Setup
app = Flask(__name__, static_folder='Images')





#################################################
# Flask Routes
#################################################


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/data_analysis.html")
def data_analysis():
    return render_template("data_analysis.html")


@app.route("/neural_network.html")
def neural_network():
    return render_template("neural_network.html")


@app.route("/random_forest.html")
def random_forest():
    return render_template("random_forest.html")


@app.route("/neural_network_code.html")
def neural_network_code():
    return render_template("neural_network_code.html")


@app.route("/random_forest_code.html")
def random_forest_code():
    return render_template("random_forest_code.html")


@app.route("/model_comparison.html")
def model_comparison():
    return render_template("model_comparison.html")


@app.route("/about_us.html")
def about_us():
    return render_template("about_us.html")


# crunching user input for approval
@app.route("/form_submit", methods=['POST'])
def crunch():

    ### DEV TOOLS ###
    return_evaluation = True


    # @TODO:
    # collecting standard items from form and making data dictionary if selection made
    general_form_data = form_dict(general_field_list)

    # collecting packed items from form and making data dictionary if selection made
    packed_form_data = form_dict(packed_field_list)

    # unpack the packs
    unpacked_form_data = unpacking(packed_form_data, packed_field_list)
    
    # appending unpacked data to general form data and sorting to model requirements
    data_package = merge_dict(field_list, general_form_data, unpacked_form_data)


    # determining to use basic or dynamic model based on user inputs
    if [item for item in data_package] == basic_model_field_list:
        basic_model = True
    else:
        basic_model = False


    # returning approval probability for user
    crunchies, model_loss, model_accuracy = credit_crunch(data_package, return_evaluation, basic_model)

    # determining approval status based on model accuracy and approval probability
    approval_status = approval_check(crunchies, model_accuracy)

    return render_template("credit_approval_results.html", approval_status=approval_status)



if __name__ == "__main__":
    if dev_mode:
        app.run(debug=True)
    else:
        app.run(debug=False)
