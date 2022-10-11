from collections import Counter
import os

from application import input_folder_path, output_folder_path, ChildSpeaker, HumanTranslator, Files


def get_val_counts(translations):
    child_counts = dict(Counter(translations.values()))
    result_dict = {}
    for key, val in translations.items():
        result_dict[key] = child_counts[val] - 1  #očekávané hodnota je o 1 menší než celkový počet výskytů 
    return result_dict

def parse_to_output(dct):
    for key, value in dct.items():
        yield f'{key} {value}'
        
def save_results(results, out_format='txt'):
    file_path = os.path.join(output_folder_path, 'output.' + out_format)
    if out_format == 'txt':
        Files.save_to_file(results, file_path)
    elif out_format == 'json':
        Files.write_json(results, file_path)
    else:
        raise ValueError("Either 'txt' or 'json' are available output formats for now.")

def run():
    input_path = Files.dialog_file_picker(
        filetype='', 
        init_dir=input_folder_path
        )
    if input_path:
        translator = HumanTranslator(ChildSpeaker())
        trans_dict = translator.translate(input_path)
        result_dict = get_val_counts(trans_dict)
        results = parse_to_output(result_dict)
        sorted_results = '\n'.join(sorted(list(results)))
        save_results(sorted_results, 'txt')



if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print(ex)
    