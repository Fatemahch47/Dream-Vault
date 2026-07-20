# # print("===================================")
# # print("        DREAMVAULT")
# # print(" Store Today, Achieve Tomorrow")
# # print("===================================")
# # print("Quote Of The Day")
# # print("Every great dream begins with a dreamer.")
# # print("===================================")

# # login={
# #     "Username":"fatima",
# #     "Password":"1234"
# # }

# # dreams={}

# # def login():

# # def add_dream():
# #     dream_id=int(input("Enter dream ID: "))
# #     dream_title=input("Enter dream title: ")
# #     category=input("Enter Dream Category: ")
# #     target_year=int(input("Enter target year: "))
# #     quote=input("Enter quote: ")
# #     notes=input("Enter your notes: ")

# #     dreams[dream_id]={
# #         "Dream Title" : dream_title,
# #         "Category": category,
# #         "Target Year": target_year,
# #         "Quote": quote,
# #         "Notes": notes,
# #         "Progress": 0,
# #         "Status": "In Progress"
# #                 }
# #     print("Dream Added Successfully")

# # def search_dream():
# #     dream_id=int(input("Enter Dream Id: "))

# #     if dream_id in dreams:
# #         print("\nDream Record")
# #         for key,value in dreams[dream_id].items():
# #             print(key,":",value)
# #     else:
# #         print("Record not found")

# # def show_dreams():
# #     if len(dreams)==0:
# #         print("No Record found")
# #     else:
# #        for dream_id, info in dreams.items():
# #            print("\nDream Id:",dream_id)
# #            for key,value in info.items():
# #                print(key,":",value)

# # def update_progress():
# #     dream_id=int(input("Enter Dream ID: "))

# #     if dream_id in dreams:
# #         progress=int(input("enter Progress(0-100):"))
# #         if progress < 0 or progress > 100:
# #             print("Invalid Progress")
# #         else:
# #             dreams[dream_id]["Progress"]=progress

# #             if progress==0:
# #                 dreams[dream_id]["Status"]="Just Started"
# #             elif progress< 50:
# #                 dreams[dream_id]["Status"]="In Progress"
# #             elif progress< 100:
# #                 dreams[dream_id]["Status"]="Almost There"
# #             else:
# #                 dreams[dream_id]["Status"]="Dream Achived"

# #             print("Progress Updated Sucessfully")
# #     else:
# #         print("Dream not found")    

# # def delete_dream():
# #     dream_id=int(input("enter dream id: "))

# #     if dream_id in dreams:
# #         del dreams[dream_id]
# #         print("Dream deleted")
# #     else:
# #         print("Dream not found")

# # def motivation_report():
# #     if len(dreams)==0:
# #         print("No dream found")
# #     else:
# #         for dream_id,info in dreams.items():
# #             print("\nDream Id:",dream_id)
# #             print("Title:",info["Dream Title"])
# #             print("Progress:",info["Progress"], "%")
# #             print("Status:",info["Status"])
# #             print("Quote:",info["Quote"])

# #             progress=info["Progress"]
# #             if progress == 0:
# #                print("Message: Every big dream starts with a small step.")
# #             elif progress < 50:
# #                print("Message: Keep going! Success is on the way.")
# #             elif progress < 100:
# #               print("Message: You are very close to achieving your dream.")
# #             else:
# #                print("Message: Congratulations! Your dream has become reality.")

# #             print("---------------------")



# # while True:
# #     print("\n==== Dream Vault ====")
# #     print("1. Add Dream")
# #     print("2. Search Dream")
# #     print("3. Show All Dreams")
# #     print("4. Update Dream Progress")
# #     print("5. Delete Dream")
# #     print("6. Motivation Report")
# #     print("8. Logi")

# #     Choice=input("enter choice:")
# #     if Choice=="1":
# #         add_dream()
# #     elif Choice=="2":
# #         search_dream()
# #     elif Choice=="3":
# #         show_dreams()
# #     elif Choice=="4":
# #         update_progress()
# #     elif Choice=="5":
# #         delete_dream()
# #     elif Choice=="6":
# #         motivation_report()
# #     elif Choice=="7":
# #         print("Thank u for using DreamVault")
# #         break
# #     else:
# #         print("Invalid choice")


class Dream:

    total_dreams = 0

    def __init__(self, title, category, year, quote, notes, favourite):
        self.title = title
        self.category = category
        self.year = year
        self.quote = quote
        self.__notes = notes
        self.favourite = favourite
        self.progress = 0
        self.status = "Just Started"

        Dream.total_dreams += 1

    @property
    def notes(self):
        return self.__notes

    def update_progress(self, progress):
        self.progress = progress

        if progress == 0:
            self.status = "Just Started"
        elif progress < 50:
            self.status = "In Progress"
        elif progress < 100:
            self.status = "Almost There"
        else:
            self.status = "Dream Achieved"

    def show(self):
        print("Dream Title:", self.title)
        print("Category:", self.category)
        print("Target Year:", self.year)
        print("Quote:", self.quote)
        print("Dream Notes:", self.notes)
        print("Favourite Dream:", self.favourite)
        print("Progress:", self.progress, "%")
        print("Status:", self.status)

    @staticmethod
    def quote_of_day():
        print("\nQuote Of The Day:")
        print("Every great dream begins with a dreamer.")

    @classmethod
    def show_total_dreams(cls):
        print("\nTotal Dreams Created:", cls.total_dreams)


class Motivation(Dream):

    def show(self):
        super().show()
        print("Motivation: Keep believing in yourself.")


dreams = {}


def add_dream():

    dream_id = int(input("Enter Dream ID: "))

    if dream_id in dreams:
        print("Dream ID already exists.")
        return

    title = input("Enter Dream Title: ")
    category = input("Enter Category: ")
    year = int(input("Enter Target Year: "))
    quote = input("Enter Quote: ")
    notes = input("Enter Notes: ")
    favourite = input("Favourite Dream (Yes/No): ")

    dream = Motivation(title, category, year, quote, notes, favourite)

    dreams[dream_id] = dream

    print("Dream Added Successfully")


def search_dream():

    dream_id = int(input("Enter Dream ID: "))

    if dream_id in dreams:
        dreams[dream_id].show()
    else:
        print("Dream Not Found")


def show_dreams():

    if len(dreams) == 0:
        print("No Dreams Found")
    else:
        for dream_id, dream in dreams.items():
            print("\nDream ID:", dream_id)
            dream.show()
            print("---------------------")


def update_progress():

    dream_id = int(input("Enter Dream ID: "))

    if dream_id in dreams:

        progress = int(input("Enter Progress (0-100): "))

        if progress < 0 or progress > 100:
            print("Invalid Progress")

        else:
            dreams[dream_id].update_progress(progress)
            print("Progress Updated Successfully")

    else:
        print("Dream Not Found")


def delete_dream():

    dream_id = int(input("Enter Dream ID: "))

    if dream_id in dreams:
        del dreams[dream_id]
        print("Dream Deleted Successfully")
    else:
        print("Dream Not Found")


def motivation_report():

    if len(dreams) == 0:
        print("No Dreams Found")

    else:
        for dream_id, dream in dreams.items():

            print("\nDream ID:", dream_id)
            print("Title:", dream.title)
            print("Progress:", dream.progress, "%")
            print("Status:", dream.status)
            print("Category:", dream.category)
            print("Target Year:", dream.year)
            print("Quote:", dream.quote)

            if dream.progress == 0:
                print("Message: Every dream starts with one step.")

            elif dream.progress < 50:
                print("Message: Keep Going!")

            elif dream.progress < 100:
                print("Message: Almost There!")

            else:
                print("Message: Congratulations! Dream Achieved!")

            print("---------------------")


def show_favourite_dreams():

    found = False

    for dream_id, dream in dreams.items():

        if dream.favourite.lower() == "yes":
            print("\nDream ID:", dream_id)
            dream.show()
            found = True

    if found == False:
        print("No Favourite Dreams Found")


def save_file():

    with open("DreamVault.txt", "w")as file:

     for dream_id, dream in dreams.items():

        file.write("Dream ID: " + str(dream_id) + "\n")
        file.write("Title: " + dream.title + "\n")
        file.write("Category: " + dream.category + "\n")
        file.write("Year: " + str(dream.year) + "\n")
        file.write("Quote: " + dream.quote + "\n")
        file.write("Notes: " + dream.notes + "\n")
        file.write("Progress: " + str(dream.progress) + "\n")
        file.write("Status: " + dream.status + "\n")
        file.write("Favourite: " + dream.favourite + "\n")
        file.write("--------------------------\n")

     print("Dream Saved successfully")

while True:

    print("\n===== DREAM VAULT =====")
    print("1. Add Dream")
    print("2. Search Dream")
    print("3. Show All Dreams")
    print("4. Update Progress")
    print("5. Delete Dream")
    print("6. Motivation Report")
    print("7. Show Favourite Dreams")
    print("8. Save Dreams To File")
    print("9. Quote Of The Day")
    print("10. Total Dreams")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_dream()

    elif choice == "2":
        search_dream()

    elif choice == "3":
        show_dreams()

    elif choice == "4":
        update_progress()

    elif choice == "5":
        delete_dream()

    elif choice == "6":
        motivation_report()

    elif choice == "7":
        show_favourite_dreams()

    elif choice == "8":
        save_file()

    elif choice == "9":
        Dream.quote_of_day()

    elif choice == "10":
        Dream.show_total_dreams()

    elif choice == "11":
        save_file()
        print("Thank you for using Dream Vault.")
        break

    else:
        print("Invalid Choice")