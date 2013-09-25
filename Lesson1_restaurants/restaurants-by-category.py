
######################

#going to create an array for each food, so that I can start seeing which ones are the best and which ones are the worst

african = []
american = []
asian = []
cajun = []
caribbean = []
chinese = []
easternEuropean = []
egyptian = []
french = []
german = []
greek = []
indian = []
indonesian = []
italian = []
japanese = []
jewish = []
korean = []
latin = []
mediterranean = []
mexican = []
middleEastern = []
russian = []
southwestern = []
thai = []
other = []
afghan = []
armenian = []
australian = []
bakery = []
bangladeshi = []
barbecue = []
basque = []
bottledBeverages = []
brazilian = []
coffee = []
californian = []
chicken = []
chilean = []
chineseCuban = []
chineseJapanese = []
continental = []
creole = []
creoleCajun = []
czech = []
delicatessen = []
vietCamMal = []
donuts = []
english = []
ethiopian = []
filipino = []
fruitsVeg = []
hamburgers = []
hawaiian = []
hotdogs = []
hotdogsPretzels = []
iceCream = []
iranian = []
irish = []
juice = []
moroccan = []
nutsConfectionary = []
pakistani = []
pancakesWaffles = []
peruvian = []
pizza = []
pizzaItalian = []
polish = []
polynesian = []
portuguese = []
salads = []
sandwiches = []
sandwichesSalads = []
scandinavian = []
seafood = []
soulFood = []
soups = []
soupsSandwiches = []
spanish = []
steak = []
tapas = []
texMex = []
turkish = []
vegetarian = []
notListed = []

for restaurant in all_restaurant_data:    
    if restaurant[7] == 02:
        african.append(restaurant)
    elif restaurant[7] == 03:
        american.append(restaurant)
    elif restaurant[7] == 05:
        asian.append(restaurant)
    elif restaurant[7] == 15:
        cajun.append(restaurant)
    elif restaurant[7] == 17:
        caribbean.append(restaurant)
    elif restaurant[7] == 20:
        chinese.append(restaurant)
    elif restaurant[7] == 30:
        easternEuropean.append(restaurant)
    elif restaurant[7] == 31:
        egyptian.append(restaurant)
    elif restaurant[7] == 35:
        french.append(restaurant)
    elif restaurant[7] == 37:
        german.append(restaurant)
    elif restaurant[7] == 38:
        greek.append(restaurant)
    elif restaurant[7] == 44:
        indian.append(restaurant)
    elif restaurant[7] == 45:
        indonesian.append(restaurant)
    elif restaurant[7] == 48:
        italian.append(restaurant)
    elif restaurant[7] == 49:
        japanese.append(restaurant)
    elif restaurant[7] == 50:
        jewish.append(restaurant)
    elif restaurant[7] == 52:
        korean.append(restaurant)
    elif restaurant[7] == 53:
        latin.append(restaurant)
    elif restaurant[7] == 54:
        mediterranean.append(restaurant)
    elif restaurant[7] == 55:
        mexican.append(restaurant)
    elif restaurant[7] == 56:
        middleEastern.append(restaurant)
    elif restaurant[7] == 67:
        russian.append(restaurant)
    elif restaurant[7] == 76:
        southwestern.append(restaurant)
    elif restaurant[7] == 82:
        thai.append(restaurant)
    elif restaurant[7] == 99:
        other.append(restaurant)
    elif restaurant[7] == 01:
        afghan.append(restaurant)
    elif restaurant[7] == 04:
        armenian.append(restaurant)
    elif restaurant[7] == 06:
        australian.append(restaurant)
    elif restaurant[7] == 08:
       bakery.append(restaurant)
    elif restaurant[7] == 09:
       bangladeshi.append(restaurant)
    elif restaurant[7] == 10:
        barbecue.append(restaurant)
    elif restaurant[7] == 11:
        basque.append(restaurant)
    elif restaurant[7] == 12:
        bottledBeverages.append(restaurant)
    elif restaurant[7] == 13:
        brazilian.append(restaurant)
    elif restaurant[7] == 14:
        coffee.append(restaurant)
    elif restaurant[7] == 16:
        californian.append(restaurant)
    elif restaurant[7] == 18:
        chicken.append(restaurant)
    elif restaurant[7] == 19:
        chilean.append(restaurant)
    elif restaurant[7] == 21:
        chineseCuban.append(restaurant)
    elif restaurant[7] == 22:
        chineseJapanese.append(restaurant)
    elif restaurant[7] == 23:
        continental.append(restaurant)
    elif restaurant[7] == 24:
        creole.append(restaurant)
    elif restaurant[7] == 25:
        creoleCajun.append(restaurant)
    elif restaurant[7] == 26:
        czech.append(restaurant)
    elif restaurant[7] == 27:
        delicatessen.append(restaurant)
    elif restaurant[7] == 28:
        vietCamMal.append(restaurant)
    elif restaurant[7] == 29:
        donuts.append(restaurant)
    elif restaurant[7] == 32:
        english.append(restaurant)
    elif restaurant[7] == 33:
        ethiopian.append(restaurant)
    elif restaurant[7] == 34:
        filipino.append(restaurant)
    elif restaurant[7] == 36:
        fruitsVeg.append(restaurant)
    elif restaurant[7] == 39:
        hamburgers.append(restaurant)
    elif restaurant[7] == 40:
        hawaiian.append(restaurant)
    elif restaurant[7] == 41:
        hotdogs.append(restaurant)
    elif restaurant[7] == 42:
        hotdogsPretzels.append(restaurant)
    elif restaurant[7] == 43:
        iceCream.append(restaurant)
    elif restaurant[7] == 46:
        iranian.append(restaurant)
    elif restaurant[7] == 46:
        irish.append(restaurant)
    elif restaurant[7] == 51:
        juice.append(restaurant)
    elif restaurant[7] == 57:
        moroccan.append(restaurant)
    elif restaurant[7] == 58:
        nutsConfectionary.append(restaurant)
    elif restaurant[7] == 59:
        pakistani.append(restaurant)
    elif restaurant[7] == 60:
        pancakesWaffles.append(restaurant)
    elif restaurant[7] == 61:
        peruvian.append(restaurant)
    elif restaurant[7] == 62:
        pizza.append(restaurant)
    elif restaurant[7] == 63:
        pizzaItalian.append(restaurant)
    elif restaurant[7] == 64:
        polish.append(restaurant)
    elif restaurant[7] == 65:
        polynesian.append(restaurant)
    elif restaurant[7] == 66:
        portuguese.append(restaurant)
    elif restaurant[7] == 68:
        salads.append(restaurant)
    elif restaurant[7] == 69:
        sandwiches.append(restaurant)
    elif restaurant[7] == 70:
        sandwichesSalads.append(restaurant)
    elif restaurant[7] == 71:
        scandinavian.append(restaurant)
    elif restaurant[7] == 72:
        seafood.append(restaurant)
    elif restaurant[7] == 73:
        soulFood.append(restaurant)
    elif restaurant[7] == 74:
        soups.append(restaurant)
    elif restaurant[7] == 75:
        soupsSandwiches.append(restaurant)
    elif restaurant[7] == 77:
        spanish.append(restaurant)
    elif restaurant[7] == 78:
        steak.append(restaurant)
    elif restaurant[7] == 80:
        tapas.append(restaurant)
    elif restaurant[7] == 81:
        texMex.append(restaurant)
    elif restaurant[7] == 83:
        turkish.append(restaurant)
    elif restaurant[7] == 84:
        vegetarian.append(restaurant)
    elif restaurant[7] == 00:
        notListed.append(restaurant)

####################################
# now let's pull out scores for each category, so we can actually compare

african_scores = []
for restaurant in african:
    african_scores.append(restaurant[11])
    break

american_scores = []
for restaurant in american:
    american_scores.append(restaurant[11])
    break   

asian_scores = []
for restaurant in asian:
    asian_scores.append(restaurant[11])

cajun_scores = []
for restaurant in cajun:
    cajun_scores.append(restaurant[11])

caribbean_scores = []
for restaurant in caribbean:
    caribbean_scores.append(restaurant[11])

chinese_scores = []
for restaurant in chinese:
    chinese_scores.append(restaurant[11])

easternEuropean_scores = []
for restaurant in easternEuropean:
    easternEuropean_scores.append(restaurant[11])

egyptian_scores = []
for restaurant in egyptian:
    egyptian_scores.append(restaurant[11])

french_scores = []
for restaurant in french:
    french_scores.append(restaurant[11])

german_scores = []
for restaurant in german:
    german_scores.append(restaurant[11])

greek_scores = []
for restaurant in greek:
    greek_scores.append(restaurant[11])

indian_scores = []
for restaurant in indian:
    indian_scores.append(restaurant[11])

indonesian_scores = []
for restaurant in indonesian:
    indonesian_scores.append(restaurant[11])

italian_scores = []
for restaurant in italian:
    italian_scores.append(restaurant[11])

japanese_scores = []
for restaurant in japanese:
    japanese_scores.append(restaurant[11])

jewish_scores = []
for restaurant in jewish:
    jewish_scores.append(restaurant[11])

korean_scores = []
for restaurant in korean:
    korean_scores.append(restaurant[11])

latin_scores = []
for restaurant in latin:
    latin_scores.append(restaurant[11])

mediterranean_scores = []
for restaurant in mediterranean:
    mediterranean_scores.append(restaurant[11])

mexican_scores = []
for restaurant in mexican:
    mexican_scores.append(restaurant[11])

middleEastern_scores = []
for restaurant in middleEastern:
    middleEastern_scores.append(restaurant[11])

russian_scores = []
for restaurant in russian:
    russian_scores.append(restaurant[11])

southwestern_scores = []
for restaurant in southwestern:
    southwestern_scores.append(restaurant[11])

thai_scores = []
for restaurant in thai:
    thai_scores.append(restaurant[11])

other_scores = []
for restaurant in other:
    other_scores.append(restaurant[11])

afghan_scores = []
for restaurant in afghan:
    afghan_scores.append(restaurant[11])

armenian_scores = []
for restaurant in armenian:
    armenian_scores.append(restaurant[11])

australian_scores = []
for restaurant in australian:
    australian_scores.append(restaurant[11])

bakery_scores = []
for restaurant in bakery:
    bakery_scores.append(restaurant[11])

bangladeshi_scores = []
for restaurant in bangladeshi:
    bangladeshi_scores.append(restaurant[11])

barbecue_scores = []
for restaurant in barbecue:
    barbecue_scores.append(restaurant[11])

basque_scores = []
for restaurant in basque:
    basque_scores.append(restaurant[11])

bottledBeverages_scores = []
for restaurant in bottledBeverages:
    bottledBeverages_scores.append(restaurant[11])

brazilian_scores = []
for restaurant in brazilian:
    brazilian_scores.append(restaurant[11])

coffee_scores = []
for restaurant in coffee:
    coffee_scores.append(restaurant[11])

californian_scores = []
for restaurant in californian:
    californian_scores.append(restaurant[11])

chicken_scores = []
for restaurant in chicken:
    chicken_scores.append(restaurant[11])

chilean_scores = []
for restaurant in chilean:
    chilean_scores.append(restaurant[11])

chineseCuban_scores = []
for restaurant in chineseCuban:
    chineseCuban_scores.append(restaurant[11])

chineseJapanese_scores = []
for restaurant in chineseJapanese:
    chineseJapanese_scores.append(restaurant[11])

continental_scores = []
for restaurant in continental:
    continental_scores.append(restaurant[11])

creole_scores = []
for restaurant in creole:
    creole_scores.append(restaurant[11])

creoleCajun_scores = []
for restaurant in creoleCajun:
    creoleCajun_scores.append(restaurant[11])

czech_scores = []
for restaurant in czech:
    czech_scores.append(restaurant[11])

delicatessen_scores = []
for restaurant in delicatessen:
    delicatessen_scores.append(restaurant[11])

vietCamMal_scores = []
for restaurant in vietCamMal:
    vietCamMal_scores.append(restaurant[11])

donuts_scores = []
for restaurant in donuts:
    donuts_scores.append(restaurant[11])

english_scores = []
for restaurant in english:
    english_scores.append(restaurant[11])

ethiopian_scores = []
for restaurant in ethiopian:
    ethiopian_scores.append(restaurant[11])

filipino_scores = []
for restaurant in filipino:
    filipino_scores.append(restaurant[11])

fruitsVeg_scores = []
for restaurant in fruitsVeg:
    fruitsVeg_scores.append(restaurant[11])

hamburgers_scores = []
for restaurant in hamburgers:
    hamburgers_scores.append(restaurant[11])

hawaiian_scores = []
for restaurant in hawaiian:
    hawaiian_scores.append(restaurant[11])

hotdogs_scores = []
for restaurant in hotdogs:
    hotdogs_scores.append(restaurant[11])

hotdogsPretzels_scores = []
for restaurant in hotdogsPretzels:
    hotdogsPretzels_scores.append(restaurant[11])

iceCream_scores = []
for restaurant in iceCream:
    iceCream_scores.append(restaurant[11])

iranian_scores = []
for restaurant in iranian:
    iranian_scores.append(restaurant[11])

irish_scores = []
for restaurant in irish:
    irish_scores.append(restaurant[11])

juice_scores = []
for restaurant in juice:
    juice_scores.append(restaurant[11])

moroccan_scores = []
for restaurant in moroccan:
    moroccan_scores.append(restaurant[11])

nutsConfectionary_scores = []
for restaurant in nutsConfectionary:
    nutsConfectionary_scores.append(restaurant[11])

pakistani_scores = []
for restaurant in pakistani:
    pakistani_scores.append(restaurant[11])

pancakesWaffles_scores = []
for restaurant in pancakesWaffles:
    pancakesWaffles_scores.append(restaurant[11])

peruvian_scores = []
for restaurant in peruvian:
    peruvian_scores.append(restaurant[11])

pizza_scores = []
for restaurant in pizza:
    pizza_scores.append(restaurant[11])

pizzaItalian_scores = []
for restaurant in pizzaItalian:
    pizzaItalian_scores.append(restaurant[11])

polish_scores = []
for restaurant in polish:
    polish_scores.append(restaurant[11])

polynesian_scores = []
for restaurant in polynesian:
    polynesian_scores.append(restaurant[11])

portuguese_scores = []
for restaurant in portuguese:
    portuguese_scores.append(restaurant[11])

salads_scores = []
for restaurant in salads:
    salads_scores.append(restaurant[11])

sandwiches_scores = []
for restaurant in sandwiches:
    sandwiches_scores.append(restaurant[11])

sandwichesSalads_scores = []
for restaurant in sandwichesSalads:
    sandwichesSalads_scores.append(restaurant[11])

scandinavian_scores = []
for restaurant in scandinavian:
    scandinavian_scores.append(restaurant[11])

seafood_scores = []
for restaurant in seafood:
    seafood_scores.append(restaurant[11])

soulFood_scores = []
for restaurant in soulFood:
    soulFood_scores.append(restaurant[11])

soups_scores = []
for restaurant in soups:
    soups_scores.append(restaurant[11])

soupsSandwiches_scores = []
for restaurant in soupsSandwiches:
    soupsSandwiches_scores.append(restaurant[11])

spanish_scores = []
for restaurant in spanish:
    spanish_scores.append(restaurant[11])

steak_scores = []
for restaurant in steak:
    steak_scores.append(restaurant[11])

tapas_scores = []
for restaurant in tapas:
    tapas_scores.append(restaurant[11])

texMex_scores = []
for restaurant in texMex:
    texMex_scores.append(restaurant[11])

turkish_scores = []
for restaurant in turkish:
    turkish_scores.append(restaurant[11])

vegetarian_scores = []
for restaurant in vegetarian:
    vegetarian_scores.append(restaurant[11])

notListed_scores = []
for restaurant in notListed:
    notListed_scores.append(restaurant[11])

####################################
# now we are going to create an array of the medians of all these categories, so we can pull out the extremes on both ends

category_scores_array = [np.ma.median(african_scores),
numpy.median(american_scores),
numpy.median(asian_scores),
numpy.median(cajun_scores),
numpy.median(caribbean_scores),
numpy.median(chinese_scores),
numpy.median(easternEuropean_scores),
numpy.median(egyptian_scores),
numpy.median(french_scores),
numpy.median(german_scores),
numpy.median(greek_scores),
numpy.median(indian_scores),
numpy.median(indonesian_scores),
numpy.median(italian_scores),
numpy.median(japanese_scores),
numpy.median(jewish_scores),
numpy.median(korean_scores),
numpy.median(latin_scores),
numpy.median(mediterranean_scores),
numpy.median(mexican_scores),
numpy.median(middleEastern_scores),
numpy.median(russian_scores),
numpy.median(southwestern_scores),
numpy.median(thai_scores),
numpy.median(other_scores),
numpy.median(afghan_scores),
numpy.median(armenian_scores),
numpy.median(australian_scores),
numpy.median(bakery_scores),
numpy.median(bangladeshi_scores),
numpy.median(barbecue_scores),
numpy.median(basque_scores),
numpy.median(bottledBeverages_scores),
numpy.median(brazilian_scores),
numpy.median(coffee_scores),
numpy.median(californian_scores),
numpy.median(chicken_scores),
numpy.median(chilean_scores),
numpy.median(chineseCuban_scores),
numpy.median(chineseJapanese_scores),
numpy.median(continental_scores),
numpy.median(creole_scores),
numpy.median(creoleCajun_scores),
numpy.median(czech_scores),
numpy.median(delicatessen_scores),
numpy.median(vietCamMal_scores),
numpy.median(donuts_scores),
numpy.median(english_scores),
numpy.median(ethiopian_scores),
numpy.median(filipino_scores),
numpy.median(fruitsVeg_scores),
numpy.median(hamburgers_scores),
numpy.median(hawaiian_scores),
numpy.median(hotdogs_scores),
numpy.median(hotdogsPretzels_scores),
numpy.median(iceCream_scores),
numpy.median(iranian_scores),
numpy.median(irish_scores),
numpy.median(juice_scores),
numpy.median(moroccan_scores),
numpy.median(nutsConfectionary_scores),
numpy.median(pakistani_scores),
numpy.median(pancakesWaffles_scores),
numpy.median(peruvian_scores),
numpy.median(pizza_scores),
numpy.median(pizzaItalian_scores),
numpy.median(polish_scores),
numpy.median(polynesian_scores),
numpy.median(portuguese_scores),
numpy.median(salads_scores),
numpy.median(sandwiches_scores),
numpy.median(sandwichesSalads_scores),
numpy.median(scandinavian_scores),
numpy.median(seafood_scores),
numpy.median(soulFood_scores),
numpy.median(soups_scores),
numpy.median(soupsSandwiches_scores),
numpy.median(spanish_scores),
numpy.median(steak_scores),
numpy.median(tapas_scores),
numpy.median(texMex_scores),
numpy.median(turkish_scores),
numpy.median(vegetarian_scores),
numpy.median(notListed_scores)]
