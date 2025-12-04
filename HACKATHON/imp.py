from bs4 import BeautifulSoup
import requests
import json 
url=['https://nutritionsource.hsph.harvard.edu/healthy-eating-plate/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/whole-grains/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/protein/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/vegetables-and-fruits/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/fats-and-cholesterol/types-of-fat/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/fats-and-cholesterol/cholesterol/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/fats-and-cholesterol/dietary-fat-and-disease/',
     'https://nutritionsource.hsph.harvard.edu/vitamins/',
     'https://nutritionsource.hsph.harvard.edu/water/',
     'https://nutritionsource.hsph.harvard.edu/healthy-drinks/other-healthy-beverage-options/',
     'https://nutritionsource.hsph.harvard.edu/healthy-drinks/drinks-to-consume-in-moderation/',
     'https://nutritionsource.hsph.harvard.edu/sports-drinks/',
     'https://nutritionsource.hsph.harvard.edu/energy-drinks/',
     'https://nutritionsource.hsph.harvard.edu/healthy-drinks/beverages-public-health-concerns/',
     'https://nutritionsource.hsph.harvard.edu/healthy-drinks/artificial-sweeteners/',
     'https://nutritionsource.hsph.harvard.edu/salt-and-sodium/',
     'https://nutritionsource.hsph.harvard.edu/salt-and-sodium/take-action-on-salt/',
     'https://nutritionsource.hsph.harvard.edu/salt-and-sodium/sodium-public-health-concerns/',
     'https://nutritionsource.hsph.harvard.edu/carbohydrates/',
     'https://nutritionsource.hsph.harvard.edu/carbohydrates/carbohydrates-and-blood-sugar/',
     'https://nutritionsource.hsph.harvard.edu/carbohydrates/fiber/',
     'https://nutritionsource.hsph.harvard.edu/carbohydrates/added-sugar-in-the-diet/',
     'https://nutritionsource.hsph.harvard.edu/sustainability/',
     'https://nutritionsource.hsph.harvard.edu/sustainability/plate-and-planet/',
     'https://nutritionsource.hsph.harvard.edu/sustainability/food-waste/',
     'https://nutritionsource.hsph.harvard.edu/healthy-weight/',
     'https://nutritionsource.hsph.harvard.edu/healthy-weight/measuring-fat/',
     'https://nutritionsource.hsph.harvard.edu/healthy-weight/best-diet-quality-counts/',
     'https://nutritionsource.hsph.harvard.edu/healthy-weight/healthy-dietary-styles/',
     'https://nutritionsource.hsph.harvard.edu/healthy-weight/diet-reviews/',
     'https://nutritionsource.hsph.harvard.edu/staying-active/',
     'https://nutritionsource.hsph.harvard.edu/staying-active/active-communities/',
     'https://nutritionsource.hsph.harvard.edu/stress-and-health/',
     'https://nutritionsource.hsph.harvard.edu/sleep/',
     'https://nutritionsource.hsph.harvard.edu/healthy-longevity/',
     'https://nutritionsource.hsph.harvard.edu/disease-prevention/',
     'https://nutritionsource.hsph.harvard.edu/obesity/',
     'https://nutritionsource.hsph.harvard.edu/obesity/preventing-obesity/',
     'https://nutritionsource.hsph.harvard.edu/disease-prevention/cardiovascular-disease/',
     'https://nutritionsource.hsph.harvard.edu/disease-prevention/cardiovascular-disease/preventing-cvd/',
     'https://nutritionsource.hsph.harvard.edu/disease-prevention/diabetes-prevention/',
     'https://nutritionsource.hsph.harvard.edu/disease-prevention/diabetes-prevention/preventing-diabetes-full-story/',
     'https://nutritionsource.hsph.harvard.edu/cancer/',
     'https://nutritionsource.hsph.harvard.edu/cancer/preventing-cancer/',
     'https://nutritionsource.hsph.harvard.edu/oral-health/',
     'https://nutritionsource.hsph.harvard.edu/precision-nutrition/',
     'https://nutritionsource.hsph.harvard.edu/nutrition-and-immunity/',
     'https://nutritionsource.hsph.harvard.edu/healthy-food-environment/',
     'https://nutritionsource.hsph.harvard.edu/healthy-child-care/',
     'https://nutritionsource.hsph.harvard.edu/healthy-schools/',
     'https://nutritionsource.hsph.harvard.edu/healthy-youth-spaces/',
     'https://nutritionsource.hsph.harvard.edu/healthy-workplaces/',
     'https://nutritionsource.hsph.harvard.edu/healthy-health-care/',
     'https://nutritionsource.hsph.harvard.edu/what-should-you-eat/',
     'https://nutritionsource.hsph.harvard.edu/healthy-drinks/'
     'https://www.healthline.com/nutrition/proven-health-benefits-of-eggs?',
     'https://www.healthline.com/health/food-nutrition?',
     'https://www.healthline.com/health/balanced-diet?',
     'https://www.webmd.com/diet/health-benefits-chicken?',
     'https://www.healthhub.sg/programmes/nutrition-hub/eat-more#protein',
     'https://www.betterhealth.vic.gov.au/health/healthyliving/water-a-vital-nutrient',
     'https://www.nhs.uk/live-well/eat-well/food-types/meat-nutrition/',
     'https://www.betterhealth.vic.gov.au/health/healthyliving/Meat-and-poultry',
     'https://www.mayoclinic.org/healthy-lifestyle/weight-loss/in-depth/weight-loss/art-20047752',
     'https://my.clevelandclinic.org/health/body/proteins',
     'https://www.medicalnewstoday.com/articles/319151#how-does-muscle-grow',
     'https://my.clevelandclinic.org/health/articles/15416-carbohydrates',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC8305097/',
     'https://www.nhlbi.nih.gov/education/dash-eating-plan',
     'https://www.nutrition.org.uk/creating-a-healthy-diet/a-healthy-balanced-diet/',
     'https://www.healthhub.sg/programmes/nutrition-hub/eat-more/',
     'https://www.healthhub.sg/well-being-and-lifestyle/food-diet-and-nutrition/the-oily-truth'
     'https://my.clevelandclinic.org/health/articles/fats',
     'https://www.health.harvard.edu/staying-healthy/the-truth-about-fats-bad-and-good',
     'https://www.medicalnewstoday.com/articles/323319#sweet-potatoes',
     'https://www.bupa.co.uk/newsroom/ourviews/food-nutrition-faqs',
     'https://www.uhhospitals.org/blog/articles/2024/01/top-10-nutrition-and-exercise-questions-answered',
     'https://www.nm.org/healthbeat/healthy-tips/nutrition/best-times-to-eat'
     ]
data=[]
for i in url:
    page=requests.get(i)
    web=BeautifulSoup(page.text,"html.parser")#gets all the html code of the website
    texts=web.find_all('p')#gets all the p(texts) parts of the website
    for p in texts:
        if len(list(p.children))>1:#removes texts with links
            continue
        if len(p.get_text())<62:
            continue
        clean_text=p.get_text()#extracts all the texts 
        data.append(clean_text)#combines all the info to a single list
    

with open("content.json","w") as f:
    json.dump(data, f,indent=2)#dumps the info to json file and indent 2 to make it look cleaner

