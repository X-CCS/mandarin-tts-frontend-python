import os


def parse_interval(file_name):
    info_dict = dict()
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        sentence_id = os.path.split(file_name)[1].split(".")[0]
        duration = float(lines[4].replace("\n", ""))
        alignment = lines[12:]
        length_alignment = len(alignment)
        alignment_info = list()
        for i in range(length_alignment // 3):
            phone_alignment = (alignment[i*3+2][1:-2],
                               (float(alignment[i*3+0][:-1]),
                                float(alignment[i*3+1][:-1])))
            alignment_info.append(phone_alignment)
        info_dict.update({"sentence_id": sentence_id,
                          "duration": duration,
                          "alignment": alignment_info})

        return info_dict


if __name__ == "__main__":
    data_path = os.path.join("BZNSYP", "PhoneLabeling")
    file_list = os.listdir(data_path)
    info_list = list()

    for file_name in file_list:
        info_list.append(parse_interval(os.path.join(data_path, file_name)))

    # get phone
    phone_set = set()
    for info in info_list:
        for alignment in info["alignment"]:
            phone_set.add(alignment[0])
    with open("phone.txt", "w", encoding="utf-8") as f:
        for phone in phone_set:
            f.write(phone + "\n")
