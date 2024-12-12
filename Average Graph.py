import matplotlib.pyplot as plt

students_names = ["Ansh" , "Darshini" , "Ashvick" , "Avni J." , "Avni P." , "Kiaan" , "Sharmistha" , "Viaan"]
students_marks = [35 , 42 , 21 , 48.5 , 43 , 20.5 , 50 , 5]

marks_perc = []

for x in students_marks:
    res = (x/50) * 100
    marks_perc.append(res)
    
print(marks_perc)

def line_chart_of_students_and_marks():
    
    plt.plot(students_names , students_marks , marker = "o" , color = "r")
    
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
    
line_chart_of_students_and_marks()

def percentage_bar_chart():
    plt.bar(students_names , marks_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
    
percentage_bar_chart()