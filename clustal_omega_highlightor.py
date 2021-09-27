
def main():
    fasta = read_fasta_file('temp_files_pre_params/fasta_files/nardini_luciferase_fragments.fasta', True)
    seq_with_indels = read_fasta_file('temp_files_pre_params/fasta_files/nardini_A_only_with_indels.fa', False)

    indel_locations = generate_indel_locals(seq_with_indels)
    new_indel_list = combine_indels(indel_locations)


    motif_dict = read_fimo_file('./temp_files_pre_params/fimo_a_only/fimo_streme_a_only/fimo.tsv')
    motif_dict2 = read_fimo_file('./temp_files_pre_params/fimo_a_only/fimo_jaspar_a_only/fimo.tsv')
    seq_dict = read_fasta_file('./temp_files_pre_params/fasta_files/nardini_luciferase_fragments_A_only.fasta', False)
    html_string = generate_html(motif_dict, motif_dict2, seq_dict, new_indel_list)

    html_string_to_output(html_string, './test.html')
    return

def generate_html(motif_dict1, motif_dict2, seq_dict, indel_dict):
    html_string = """
    <!DOCTYPE html>
    <html lang="en-US">
    <head>
        <title>Html Conversion</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="Keywords"
        content="HTML">
        <meta name="Description"
          content="This is a highlighted FIMO output thingy">
    </head>
    <body>
    <h> Legend: </h>
    <div style="background:Aqua; width:75%;"> This is for fimo run with streme.txt as the motif file </div>
    <div style="background:PaleVioletRed; width:75%"> This is for fimo run with JASPAR as the motif file </div>
    <div style="background:Plum; width:75%"> This is for when those highlighted motifs overlap </div>
     """
    dynamic_html_string = None
    motif_keys = list(motif_dict1.keys())
    motif_keys.sort()
    print("In ourput")
    for key in motif_keys:
        if dynamic_html_string == None:
            dynamic_html_string = """<p style="font-family:'Courier New'; word-wrap: break-word; width: 75%">"""
        else:
            dynamic_html_string += """<p style="font-family:'Courier New'; word-wrap: break-word; width: 75%">"""
        dynamic_html_string += ">" + str(key) + "<br>"

        indel_list = indel_dict[key]

        #if key == "KLF_Fd09_1_A":
         #   print(indel_list)

        sequence = seq_dict[key]
        highlight_list = motif_dict1[key]
        highlight_list = sorted(highlight_list, key=lambda x: x[0])
        overlap_dict = {}
        
        highlight_overlaps(highlight_list, overlap_dict, "blue")

        highlight_list2 = motif_dict2[key]
        highlight_list2 = sorted(highlight_list2, key=lambda x: x[0])
        
        highlight_overlaps(highlight_list2, overlap_dict, "red")
        if "OVO_Fd03_8_A" in key:
            print(len(sequence))
        for index, char in enumerate(sequence):
            index_1_based = index + 1
            if index_1_based in overlap_dict:
                color = overlap_dict[index_1_based]
            else:
                color = "none"

            for pos, string in indel_list:
                if pos == index:
                    if (index_1_based - 1) in overlap_dict and (index_1_based + 1) in overlap_dict:
                        print(overlap_dict[(index_1_based - 1)], color, overlap_dict[(index_1_based + 1)])
                    dynamic_html_string += string
                    break

            if color == "purple":
                dynamic_html_string += '<span style="background:Plum;">'
                dynamic_html_string += char.upper()
                dynamic_html_string += "</span>"
            elif color == "red":
                dynamic_html_string += '<span style="background:PaleVioletRed;">'
                dynamic_html_string += char.upper()
                dynamic_html_string += "</span>"
            elif color == "blue":
                dynamic_html_string += '<span style="background:Aqua;">'
                dynamic_html_string += char.upper()
                dynamic_html_string += "</span>"
            else:
                dynamic_html_string += char.upper()

        dynamic_html_string += "\n</p>"

    html_string += dynamic_html_string
    html_string += '\n</body>'
    return html_string

def combine_indels(indel_dict):
    new_indel_dict = {}
    keys = list(indel_dict.keys())
    for key in keys:
        new_indel_dict[key] = []
        indel_list = indel_dict[key]
        start_location = indel_list[0]
        indel_width = 1
        for index, location in enumerate(indel_list):
            if index + 1 >= len(indel_list):
                break
            elif int(indel_list[index + 1]) - int(indel_list[index]) == 1:
                    if indel_width == 1:
                        start_location = location
                    indel_width += 1
            elif indel_width > 0:
                if indel_width == 1:
                    start_location = location
                start_location = calibrate_start_location(start_location, new_indel_dict, key)
                create_add_indel(new_indel_dict, key, start_location - 1, indel_width)                
                indel_width = 1
                    
    return new_indel_dict

def calibrate_start_location(start_location, new_indel_dict, key):
    indels_in_key = new_indel_dict[key]
    total_length_of_indels = 0
    for indel in indels_in_key:
        indel_string = indel[1]
        str_len = len(indel_string)
        total_length_of_indels += str_len
    
    return start_location - total_length_of_indels

def create_add_indel(new_indel_dict, key, start_location, indel_width):
    indel_string = ""
    for x in range(indel_width):
        indel_string += "-"
    new_indel_dict[key].append((start_location, indel_string))
    #print(start_location, indel_string, indel_width)
    #if key == 'OVO_Fd03_8_A':
        #print(start_location, indel_string, indel_width)

def generate_indel_locals(seqs_with_indels):
    keys = list(seqs_with_indels.keys())
    indel_locations = {}
    for key in keys:
        if key not in indel_locations:
            indel_locations[key] = []
        
        seq = seqs_with_indels[key]
        for index, char in enumerate(seq):
            if char == '-':
                indel_locations[key].append(index + 1)

    return indel_locations

def html_string_to_output(html_string, outputdir):
    output = open(outputdir, 'w')
    output.write(html_string)
    output.close

def output_A_seqs(fasta, output, keys):
    for key in keys:
        seq = fasta[key]
        temp_output_string = ">" + key + "\n"
        for index, char in enumerate(seq):
            if index % 80 == 0 and index > 0:
                temp_output_string += "\n"
                temp_output_string += char
            else:
                temp_output_string += char

        output.write(temp_output_string + '\n\n\n')
    output.close()

def read_fasta_file(file_path, only_A):
    sequence_dictionary = {}
    sequence = None
    sequence_name = None
    with open(file_path) as f:
        for line in f:
            if '>' in line:
                header = line
                split_header = header.split()                   

                if sequence_name == None:
                    sequence = None
                    sequence_name = split_header[0]
                    sequence_name = sequence_name[1:]
                else:
                    if ('_A' or '_a') in sequence_name or not only_A:
                        sequence_dictionary[sequence_name] = sequence
                    sequence_name = split_header[0]
                    sequence_name = sequence_name[1:]
                    sequence = None
            else:
                if sequence == None:
                    sequence = line.strip()
                else:
                    sequence += line.strip() 
    if ('_A' or '_a') in sequence_name or not only_A:
        sequence_dictionary[sequence_name] = sequence
    return sequence_dictionary

def read_fimo_file(file_path):
    sequence_name_dict = {}
    with open(file_path) as f:
            header = f.readline() #to get rid of it
            for line in f:
                if len(line) <= 1:
                    return sequence_name_dict
                line_split = line.split()
                seq_name = line_split[2]
                start = line_split[3]
                stop = line_split[4]

                if seq_name not in sequence_name_dict:
                    sequence_name_dict[seq_name] = []
                    sequence_name_dict[seq_name].append((start, stop))
                else:
                    sequence_name_dict[seq_name].append((start, stop))  
    return sequence_name_dict

def highlight_overlaps(highlight_list, overlap_dict, color):
    for highlight in highlight_list:
            start, end = highlight
            for x in range(int(start), int(end) + 1):
                if x in overlap_dict:
                    ch_color = overlap_dict[x]
                    if color != ch_color:
                        overlap_dict[x] = "purple"
                else:
                    overlap_dict[x] = color

main()