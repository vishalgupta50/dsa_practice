def image_processing():
    images = []
    while True:
        try:
            line = input()
            fields = line.split()
            item = {
                'count': int(fields[0]),
                'files': fields[1:]
            }
            if item["count"] == 1:
                # insert(item["files"])
                if item["files"] in images:
                    print("Image with same name already exists")
                else:
                    index = 0
                    while index < len(images) and item["files"] > images[index]:
                        index += 1
                    images.insert(index, item["files"])
            print(images)
            # elif item["count"] == 2:
            #     delete(item["files"])
            # elif item["count"] == 3:
            #     rename(item["files"])
            # elif item["count"] == 4:
            #     print_list()
            # data.append(item)
        except:
            break





    print("hello")


if __name__ == "__main__":
    # length = int(input())
    # instructions = input()
    image_processing()


    # print(data)





