from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

data = {
   'receiver': '',
   'repeated': False
}

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/onetime-form", methods=['GET', 'POST'])
def onetime_form():
   res = request.form.to_dict()
   
   #get data when is a response
   if (res):
      data.update({
         'receiver': res['receiver'],
         'repeated': False,
         'date': res['date']
      })
   print(data)
   return render_template("single-form.html")

@app.route("/repeated-form", methods=['GET', 'POST'])
def repeated_form():
   res = request.form.to_dict()
   #get data when is a response
   if (res):
      data.update({
         'receiver': res['receiver'],
         'repeated': True,
         'period': res['period'],
      })
      #condition when there is a specific date
      if(res.get('date')):
         data['date'] = res['date'];
      elif (data.get('date')): #when no date specified but there is a date in prev state
         data.pop('date') #remove prev date
   print(data)
   return render_template("repeated-form.html")

if __name__ == '__main__':
    app.run(debug=True)
    
#  data usages:
#     ['receiver']: receiver email ->String
#     ['repeated']: False if one-time, True if repeated ->Bool
#     ['date']: ->String
#        - Specific date (One-time)
#        - Scheduling dates (Repeated)
#           + 'monday' to 'sunday' for every week and fortnight
#           + '1' to '31' for every month (have to use int() if needed)
#           + Specific date (like one-time) for every year
#     ['period']: (Repeated ONLY) ->String
#        - e-day: everyday
#        - e-month: every month
#        - e-fortnight: every fortnight
#        - e-week: every week
#        - e-year: every year
#  **NOTE** Try to run the main.py before merging to the project.