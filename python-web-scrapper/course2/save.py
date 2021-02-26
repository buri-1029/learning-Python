import csv


def save_to_file():
    file = open("course2/jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company",
                     "location", "link"])
    # for job in jobs:
    #     # jobs => dictionary
    #     # job.valuse() => dict.value만 가져올 수 있음
    #     # list(job.valuse())로 감싸서 리스트로 만들어서
    #     # job이 가진 값의 리스트를 row로 가져오게 되도록
    #     writer.writerow(list(job.values()))
    return
