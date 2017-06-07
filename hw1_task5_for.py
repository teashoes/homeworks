##### 5 посчитать средние значения ####
school_data = [
    {'class': '4a', 'scores': [3,4,4,5,2]}, 
    {'class':'4b', 'scores': [3,5,6,5,2]}, 
    {'class':'4v', 'scores': [3,4,2,3,2]}
]

avg_scores=[] #заведем список куда запишем значения 
for class_data in school_data:
    print(class_data['class'], sum(class_data['scores'])/len(class_data['scores']))
    avg_scores.append(sum(class_data['scores'])/len(class_data['scores']))
print(round(sum(avg_scores)/len(school_data), 1))
