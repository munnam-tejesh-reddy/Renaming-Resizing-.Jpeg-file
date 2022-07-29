import cv2
import os
# creating a list of all folders//files to be renamed
val = ['adhirasam',
'aloo_gobi',
'aloo_matar',
'aloo_methi',
'aloo_shimla_mirch',
'aloo_tikki',
'anarsa',
'apple_pie',
'ariselu',
'bandar_laddu',
'basundi',
'beet_salad',
'bhatura',
'bhindi_masala',
'biriyani',
'boondi',
'bread_pudding',
'breakfast_burrito',
'bruschetta',
'butter_chicken',
'caesar_salad',
'cannoli',
'caprese_salad',
'carrot_cake',
'chak_hao_kheer',
'cham_cham',
'chana_masala',
'chapati',
'cheese_plate',
'cheesecake',
'chhena_kheeri',
'chicken_curry',
'chicken_quesadilla',
'chicken_razala',
'chicken_tikka',
'chicken_tikka_masala',
'chicken_wings',
'chikki',
'chocolate_cake',
'chocolate_mousse',
'club_sandwich',
'creme_brulee',
'cup_cakes',
'daal_baati_churma',
'daal_puri',
'dal_makhani',
'dal_tadka',
'deviled_eggs',
'dharwad_pedha',
'donuts',
'doodhpak',
'double_ka_meetha',
'dum_aloo',
'dumplings',
'edamame',
'eggs_benedict',
'falafel',
'fish_and_chips',
'french_fries',
'french_onion_soup',
'french_toast',
'fried_calamari',
'fried_rice',
'frozen_yogurt',
'gajar_ka_halwa',
'garlic_bread',
'gavvalu',
'ghevar',
'gnocchi',
'greek_salad',
'grilled_cheese_sandwich',
'grilled_salmon',
'guacamole',
'guacamole',
'gyoza',
'hamburger',
'hot_and_sour_soup',
'hot_dog',
'huevos_rancheros',
'hummus',
'ice_cream',
'imarti',
'jalebi',
'kachori',
'kadai_paneer',
'kadhi_pakoda',
'kajjikaya',
'kakinada_khaja',
'kalakand',
'karela_bharta',
'kofta',
'kuzhi_paniyaram',
'lasagna',
'lassi',
'ledikeni',
'litti_chokha',
'lyangcha',
'maach_jhol',
'macaroni_and_cheese',
'macarons',
'makki_di_raoti_saroson_da_saag',
'malapua',
'misi_roti',
'miso_soup',
'modak',
'mysore_pak',
'naan',
'nachos',
'navratthan_khorma',
'omelette',
'onion_rings',
'pad_thai',
'palak_panner',
'pancakes',
'paneer_butter_masala',
'panna_cotta',
'phirni',
'pithe',
'pizza',
'poha',
'poornalu',
'pootharekulu',
'pork_chop',
'poutine',
'prime_rib',
'qubani_ka_meetha',
'rabri',
'ramen',
'ras_malai',
'rasgulla',
'ravioli',
'red_velvet_cake',
'risotto',
'samosa',
'sandhesh',
'seaweed_salad',
'shankarpali',
'sheer_korma',
'sheera',
'shrikhand',
'shrimp_and_grits',
'sohan_halwa',
'sohan_papdi',
'spaghetti_bolognese',
'spaghetti_carbonara',
'spring_rolls',
'steak',
'strawberry_shortcake',
'sutar_feni',
'tacos',
'tiramisu',
'tuna_tartare',
'unni_appam',
'waffles',]


file = 'C://Users//DELL//Desktop//Food waste project data//Images Renaming + Code//images' # this is the main path

k=1 # For name the file inthe sub folders in sequential order

if not os.path.exists(file+"//output"): # checking if the file exists, and creating the folder
        os.makedirs(file+"//output")

for i in val:

    path = file + '//' + i # path of individual folders

    new_file = "//output//"  + i # here are the output folders
    
    dir = file + new_file
    if not os.path.exists(dir): # checking for each folder exists or not and creating a folder
        os.makedirs(dir)
    
    name = os.listdir(path)
    
    for j in name:
        img = cv2.imread(path+"//"+j)
        img1 = cv2.resize(img, (300, 300),
               interpolation = cv2.INTER_NEAREST)
        print (img1.shape)
        rename = dir+'//'+str(k)+'.jpg'
        cv2.imwrite(rename, img1)# renaming file using k

        k= k+1


print('Mission complete')


       
