import os
from PIL import Image
import json

def extract_positive_prompts():
    # Directory corrente in cui si trova lo script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Formati di file immagine supportati
    supported_formats = ['.png']  # I metadati dettagliati sono più probabili nei PNG

    # Scansiona tutti i file nella directory corrente
    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)

        # Verifica se il file è un'immagine supportata
        if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in supported_formats):
            try:
                # Apri l'immagine con PIL
                with Image.open(file_path) as img:
                    # Leggi i metadati del file PNG
                    metadata = img.info

                    # Verifica se esiste un campo "prompt" nei metadati
                    raw_prompt_data = metadata.get("prompt", None)

                    if raw_prompt_data:
                        try:
                            # Carica i metadati come JSON
                            prompt_data = json.loads(raw_prompt_data)

                            # Cerca il prompt positivo all'interno della struttura
                            for key, value in prompt_data.items():
                                if value.get('class_type') == 'ComfyUIStyler':
                                    inputs = value.get('inputs', {})
                                    positive_prompt = inputs.get('text_positive', None)

                                    if positive_prompt:
                                        # Crea un file .txt per salvare il prompt positivo
                                        txt_filename = os.path.splitext(filename)[0] + '.txt'
                                        txt_path = os.path.join(current_dir, txt_filename)

                                        with open(txt_path, 'w', encoding='utf-8') as txt_file:
                                            txt_file.write(positive_prompt)

                                        print(f"Prompt positivo salvato: {txt_filename}")
                                    else:
                                        print(f"Nessun prompt positivo trovato per: {filename}")
                        except json.JSONDecodeError:
                            print(f"Metadati 'prompt' non in formato JSON per: {filename}")
                    else:
                        print(f"Nessun metadato 'prompt' trovato per: {filename}")

            except Exception as e:
                print(f"Errore con il file {filename}: {e}")

if __name__ == "__main__":
    extract_positive_prompts()
