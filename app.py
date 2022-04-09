import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

df_1 = pd.read_csv("first_telc_cleaned.csv")

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    """
    SeniorCitizen
    MonthlyCharges
    TotalCharges
    gender
    Partner
    Dependents
    PhoneService
    MultipleLines
    InternetService
    OnlineSecurity
    OnlineBackup
    DeviceProtection
    TechSupport
    StreamingTV
    StreamingMovies
    Contract
    PaperlessBilling
    PaymentMethod
    tenure
    """

    Seniorcitizen = int(request.form.get("query1"))
    Monthlycharges = float(request.form.get("query2"))
    Totalcharges = float(request.form.get("query3"))
    Gender = request.form.get("query4")
    Partner = request.form.get("query5")
    Dependents = request.form.get("query6")
    Phoneservice = request.form.get("query7")
    Multiplelines = request.form.get("query8")
    Internetservice = request.form.get("query9")
    Onlinesecurity = request.form.get("query10")
    Onlinebackup = request.form.get("query11")
    Deviceprotection = request.form.get("query12")
    Techsupport = request.form.get("query13")
    Streamingtv = request.form.get("query14")
    Streamingmovies = request.form.get("query15")
    Contracttype = request.form.get("query16")
    Paperlessbilling = request.form.get("query17")
    Paymentmethod = request.form.get("query18")
    Tenure = int(request.form.get("query19"))
    print(Seniorcitizen,
            Monthlycharges,
            Totalcharges,
            Gender,
            Partner,
            Dependents,
            Phoneservice,
            Multiplelines,
            Internetservice,
            Onlinesecurity,
            Onlinebackup,
            Deviceprotection,
            Techsupport,
            Streamingtv,
            Streamingmovies,
            Contracttype,
            Paperlessbilling,
            Paymentmethod,
            Tenure)
    #Gender
    if Gender=="Male":
        gender_Male = 1
        gender_Female = 0
    else:
        gender_Female = 1
        gender_Male = 0
    
    #Partner
    if Partner=="Yes":
        Partner_Yes = 1
        Partner_No = 0
    else:
        Partner_No = 1
        Partner_Yes = 0

    #Dependents
    if Dependents=="Yes":
        Dependents_Yes = 1
        Dependents_No = 0
    else:
        Dependents_No = 1
        Dependents_Yes = 0

    #Phoneservice
    if Phoneservice=="Yes":
        PhoneService_Yes = 1
        PhoneService_No = 0
    else:
        PhoneService_No = 1
        PhoneService_Yes = 0

    #MultipleLines
    if Multiplelines=="Yes":
        MultipleLines_Yes = 1
        MultipleLines_No = 0
        MultipleLines_No_phone_service = 0
    elif Multiplelines=="No":
        MultipleLines_Yes = 0
        MultipleLines_No = 1
        MultipleLines_No_phone_service = 0

    else:
        MultipleLines_Yes = 0
        MultipleLines_No = 1
        MultipleLines_No_phone_service = 1

    #Internet Service
    if Internetservice =="DSL":
        InternetService_DSL = 1
        InternetService_Fiber_optic = 0
        InternetService_No = 0
    elif Internetservice =="Fiber_optic":
        InternetService_DSL = 0
        InternetService_Fiber_optic = 1
        InternetService_No = 0
    else:
        InternetService_DSL = 0
        InternetService_Fiber_optic = 0
        InternetService_No = 1

    # Online Security
    if Onlinesecurity == "Yes":
        OnlineSecurity_Yes = 1
        OnlineSecurity_No_internet_service = 0
        OnlineSecurity_No = 0
    elif Onlinesecurity == "No":
        OnlineSecurity_Yes = 0
        OnlineSecurity_No_internet_service = 0
        OnlineSecurity_No = 1
    else:
        Onlinesecurity == "No_internet_service"
        OnlineSecurity_Yes = 1
        OnlineSecurity_No_internet_service = 0
        OnlineSecurity_No = 0

    # Online Backup
    if Onlinebackup == 'Yes':
        OnlineBackup_Yes = 1
        OnlineBackup_No_internet_service = 0
        OnlineBackup_No = 0
    elif Onlinebackup == 'No':
        OnlineBackup_Yes = 0
        OnlineBackup_No_internet_service = 0
        OnlineBackup_No = 1
    else:
        Onlinebackup == 'No_internet_service'
        OnlineBackup_Yes = 0
        OnlineBackup_No_internet_service = 1
        OnlineBackup_No = 0

    # Device Protection
    if Deviceprotection == 'Yes':
        DeviceProtection_Yes = 1
        DeviceProtection_No_internet_service = 0
        DeviceProtection_No = 0
    elif Deviceprotection == 'No':
        DeviceProtection_Yes = 0
        DeviceProtection_No_internet_service = 0
        DeviceProtection_No = 1
    else:
        Deviceprotection == 'No_internet_service'
        DeviceProtection_Yes = 0
        DeviceProtection_No_internet_service = 1
        DeviceProtection_No = 0

    # Tech Support
    if Techsupport == 'Yes':
        TechSupport_Yes = 1
        TechSupport_No_internet_service = 0
        TechSupport_No = 0
    elif Techsupport == 'No':
        TechSupport_Yes = 0
        TechSupport_No_internet_service = 0
        TechSupport_No = 1
    else:
        Techsupport == 'No_internet_service'
        TechSupport_Yes = 0
        TechSupport_No_internet_service = 1
        TechSupport_No = 0


    # Streaming TV
    if Streamingtv == 'Yes':
        StreamingTV_Yes = 1
        StreamingTV_No_internet_service = 0
        StreamingTV_No = 0
    elif Streamingtv == 'No':
        StreamingTV_Yes = 0
        StreamingTV_No_internet_service = 0
        StreamingTV_No = 1
    else:
        Streamingtv == 'No_internet_service'
        StreamingTV_Yes = 0
        StreamingTV_No_internet_service = 1
        StreamingTV_No = 0

    # Streaming Movies
    if Streamingmovies == 'Yes':
        StreamingMovies_Yes = 1
        StreamingMovies_No_internet_service = 0
        StreamingMovies_No = 0
    elif Streamingmovies == 'No':
        StreamingMovies_Yes = 0
        StreamingMovies_No_internet_service = 0
        StreamingMovies_No = 1
    else:
        Streamingmovies == 'No_internet_service'
        StreamingMovies_Yes = 0
        StreamingMovies_No_internet_service = 1
        StreamingMovies_No = 0

    # Contract
    if Contracttype == 'Month_to_month':
        Contract_Month_to_month = 1
        Contract_One_year = 0
        Contract_Two_year = 0
    elif Contracttype == 'One_year':
        Contract_Month_to_month = 0
        Contract_One_year = 1
        Contract_Two_year = 0
    else:
        Contracttype == 'Two_year'
        Contract_Month_to_month = 0
        Contract_One_year = 0
        Contract_Two_year = 1

    # Paperless billing
    if Paperlessbilling == 'Yes':
        PaperlessBilling_No = 0
        PaperlessBilling_Yes = 1

    else:
        PaperlessBilling_No = 1
        PaperlessBilling_Yes = 0

    # Payment method
    if Paymentmethod == 'Bank_transfer_automatic':
        PaymentMethod_Bank_transfer_automatic = 1
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
    elif Paymentmethod == 'Credit_card_automatic':
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_Credit_card_automatic = 1
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 0
    elif Paymentmethod == 'Electronic_check':
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 1
        PaymentMethod_Mailed_check = 0
    else:
        PaymentMethod_Bank_transfer_automatic = 0
        PaymentMethod_Credit_card_automatic = 0
        PaymentMethod_Electronic_check = 0
        PaymentMethod_Mailed_check = 1

    if Tenure in range(1,13):
        tenure_group_1_12 = 1
        tenure_group_13_24 = 0
        tenure_group_25_36 = 0
        tenure_group_37_48 = 0
        tenure_group_49_60 = 0
        tenure_group_61_72 =0
    elif Tenure in range(13,25):
        tenure_group_1_12 = 0
        tenure_group_13_24 = 1
        tenure_group_25_36 = 0
        tenure_group_37_48 = 0
        tenure_group_49_60 = 0
        tenure_group_61_72 =0
    elif Tenure in range(25,37):
        tenure_group_1_12 = 0
        tenure_group_13_24 = 0
        tenure_group_25_36 = 1
        tenure_group_37_48 = 0
        tenure_group_49_60 = 0
        tenure_group_61_72 =0
    elif Tenure in range(37,49):
        tenure_group_1_12 = 0
        tenure_group_13_24 = 0
        tenure_group_25_36 = 0
        tenure_group_37_48 = 1
        tenure_group_49_60 = 0
        tenure_group_61_72 =0
    elif Tenure in range(49,61):
        tenure_group_1_12 = 0
        tenure_group_13_24 = 0
        tenure_group_25_36 = 0
        tenure_group_37_48 = 0
        tenure_group_49_60 = 1
        tenure_group_61_72 =0
    else:
        tenure_group_1_12 = 0
        tenure_group_13_24 = 0
        tenure_group_25_36 = 0
        tenure_group_37_48 = 0
        tenure_group_49_60 = 0
        tenure_group_61_72 =1

    data_vid = {'SeniorCitizen':[Seniorcitizen],'tenure':[Tenure],'MonthlyCharges':[Monthlycharges],'TotalCharges':[Totalcharges],'gender_Female':[gender_Female],'gender_Male':[gender_Male],'Partner_No':[Partner_No],'Partner_Yes':[Partner_Yes],'Dependents_No':[Dependents_No],'Dependents_Yes':[Dependents_Yes],'PhoneService_No':[PhoneService_No],'PhoneService_Yes':[PhoneService_Yes],'MultipleLines_No':[MultipleLines_No],'MultipleLines_No_phone_service':[MultipleLines_No_phone_service],'MultipleLines_Yes':[MultipleLines_Yes],'InternetService_DSL':[InternetService_DSL],'InternetService_Fiber_optic':[InternetService_Fiber_optic],'InternetService_No':[InternetService_No],'OnlineSecurity_No':[OnlineSecurity_No],'OnlineSecurity_No_internet_service':[OnlineSecurity_No_internet_service],'OnlineSecurity_Yes':[OnlineSecurity_Yes],'OnlineBackup_No':[OnlineBackup_No],'OnlineBackup_No_internet_service':[OnlineBackup_No_internet_service],'OnlineBackup_Yes':[OnlineBackup_Yes],'DeviceProtection_No':[DeviceProtection_No],'DeviceProtection_No_internet_service':[DeviceProtection_No_internet_service],'DeviceProtection_Yes':[DeviceProtection_Yes],'TechSupport_No':[TechSupport_No],'TechSupport_No_internet_service':[TechSupport_No_internet_service],'TechSupport_Yes':[TechSupport_Yes],'StreamingTV_No':[StreamingTV_No],'StreamingTV_No_internet_service':[StreamingTV_No_internet_service],'StreamingTV_Yes':[StreamingTV_Yes],'StreamingMovies_No':[StreamingMovies_No],'StreamingMovies_No_internet_service':[StreamingMovies_No_internet_service],'StreamingMovies_Yes':[StreamingMovies_Yes],'Contract_Month_to_month':[Contract_Month_to_month],'Contract_One_year':[Contract_One_year],'Contract_Two_year':[Contract_Two_year],'PaperlessBilling_No':[PaperlessBilling_No],'PaperlessBilling_Yes':[PaperlessBilling_Yes],'PaymentMethod_Bank_transfer_automatic':[PaymentMethod_Bank_transfer_automatic],'PaymentMethod_Credit_card_automatic':[PaymentMethod_Credit_card_automatic],'PaymentMethod_Electronic_check':[PaymentMethod_Electronic_check],'PaymentMethod_Mailed_check':[PaymentMethod_Mailed_check],'tenure_group_1_12':[tenure_group_1_12],'tenure_group_13_24':[tenure_group_13_24],'tenure_group_25_36':[tenure_group_25_36],'tenure_group_37_48':[tenure_group_37_48],'tenure_group_49_60':[tenure_group_49_60],'tenure_group_61_72':[tenure_group_61_72]
    }

    df_vid = pd.DataFrame.from_dict(data_vid)

    model = pickle.load(open("model_rf.sav", "rb"))
    
    single = model.predict(df_vid)
    # print("Single value: {}".format(single))
    probablity = model.predict_proba(df_vid)[:,1]
    # print("Proba value: {}".format(probablity))

    if single == 1:
        o1 = "This customer is likely to be churned, require appropriate customer retention strategies."
        o2 = "Confidence: {}".format(probablity * 100)
    else:
        o1 = "This customer is likely to continue!"
        o2 = "Confidence: {}".format(probablity * 100)

    return render_template(
        "index.html",
        output1=o1,
        output2=o2,
        Seniorcitizen=int(request.form.get("query1")),
        Monthlycharges=float(request.form.get("query2")),
        Totalcharges=float(request.form.get("query3")),
        Gender=request.form.get("query4"),
        Partner=request.form.get("query5"),
        Dependents=request.form.get("query6"),
        Phoneservice=request.form.get("query7"),
        Multiplelines=request.form.get("query8"),
        Internetservice=request.form.get("query9"),
        Onlinesecurity=request.form.get("query10"),
        Onlinebackup=request.form.get("query11"),
        Deviceprotection=request.form.get("query12"),
        Techsupport=request.form.get("query13"),
        Streamingtv=request.form.get("query14"),
        Streamingmovies=request.form.get("query15"),
        Contracttype=request.form.get("query16"),
        Paperlessbilling=request.form.get("query17"),
        Paymentmethod=request.form.get("query18"),
        Tenure=int(request.form.get("query19")),
    )


if __name__ == "__main__":
    app.run(debug=True)
