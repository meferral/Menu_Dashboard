# Menu_Dashboard

## MVP, Goal and Purpose
The motivation for my capstone is to create a dashboard to have real time data for operators on which areas are driving their cost per meal (CPM= how much it costs in food per customer).  
-	Data Question- How can we get NetMenu data to be displayed with visuals and have it updated with Meal Plan reports coming out of Gold daily?
-	Data to be Used- we will use the menu export from NetMenu, the daily swipe reports out of Gold, as well as operator generated forecasted numbers

The ultimate purpose is for operators to be able have a central spot to get the information they need and allow them to make better decisions without having to run reports out of the system OR giving them a better idea of what reports they need to look at.  

KPI’s that will be focused on the dashboard will be CPM and food waste.

How can we:
look at in real time what our CPM is and what is driving that cost?
make better decisions about our menu mix that touch on the areas that we deem important (socially responsible menuing) and still keep costs in line?
look at in real time what our CPM is and what is driving that cost?

# MVP
The minimum viable product will be a PowerBI dashboard that updates when new information is available so that decisions can be made in real time.

## Technologies & Workflow
1.  **Outlook** receives email system generated process that runs at end of daily
2.  **Power Automate** scrapes the CSV from the email and moves it to a Onedrive folder
3.  **Python**
      - reads in the entire folder using the `os` and `glob` libraries to continually concatenate the files as they get added to the folder   
      - cleans the files so they can be displayed for analysis and then exports one concise excel file to be picked up by PowerBI
      - this is run using the `time` and `schedule` libraries for automation
4.  **PowerBI** desktop houses the cleaned data and manages the data relationships as well as pulls in hardcoded data with forecasting information.
      - DAX functions are used to create KPI's on the dashboard and those are housed on their own tables(2)
5.  **On Premises Gateway** connects the web based PowerBI with local folders so that the above processes flow through to the front end users

## Definitions
- **NetMenu**- Menu management software
- **Gold**- Card service software
- **Cost Per Meal** = Total cost of food on the menu / # of customers that come through the door
- **Forecasted Amount/Cost**- a educated guess on amounts to produce
- **Prepared Amount/Cost**- the amount that got recorded for production in a real setting
- **Served Amount/Cost**- the food that was served from the prepared
- **Leftover Amount/Cost**- the difference of the prepared and served cost/amount

PowerBI link to dashboard:  https://app.powerbi.com/links/pIkHS6IC4-?ctid=ba5a7f39-e3be-4ab3-b450-67fa80faecad&pbi_source=linkShare&bookmarkGuid=597196a1-1986-407b-b317-9985cb73dcb6


>>>>>>> c713d651cb8fa5f908ff1dc32e95d6bb18d36583
