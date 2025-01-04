# Extract Positive Prompts - Estrattore di Prompt Positivi

Questo script Python è progettato per estrarre i prompt positivi dai metadati delle immagini PNG generate con ComfyUI. Lo script analizza tutte le immagini PNG nella directory corrente ed estrae i prompt positivi, salvandoli in file di testo separati.

## Prerequisiti

- Python 3.6 o superiore
- pip (gestore pacchetti Python)

## Installazione

1. Clona il repository o scarica lo script

```bash
git clone https://github.com/Tranchillo/Extract_PositivePrompts_Metadata
cd Extract_PositivePrompts_Metadata
```

2. (Consigliato) Crea e attiva un ambiente virtuale

Per Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

Per Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installa le dipendenze richieste

```bash
pip install pillow
```

## Utilizzo

1. Posiziona lo script nella stessa directory delle immagini PNG da processare
2. Esegui lo script:

```bash
python Extract_PositivePrompts_Metadata.py
```

Lo script:
- Scansionerà tutti i file PNG nella directory corrente
- Estrarrà i prompt positivi dai metadati delle immagini generate con ComfyUI
- Creerà un file .txt per ogni immagine contenente il prompt positivo
- Il nome del file di testo sarà lo stesso dell'immagine originale ma con estensione .txt

## Output

Per ogni immagine processata con successo, verrà creato un file .txt contenente il prompt positivo. Lo script mostrerà anche messaggi di stato nel terminale per indicare:
- Quali file sono stati processati con successo
- Quali file non contengono prompt positivi
- Eventuali errori durante il processamento

## Note

- Lo script supporta attualmente solo file PNG
- I metadati devono essere nel formato specifico utilizzato da ComfyUI
- Se un'immagine non contiene metadati validi o prompt positivi, verrà mostrato un messaggio appropriato

## Risoluzione problemi

Se incontri errori durante l'esecuzione dello script, verifica che:
- Le immagini siano nel formato PNG
- Le immagini contengano metadati validi di ComfyUI
- Python e le dipendenze richieste siano installati correttamente
- Lo script sia nella stessa directory delle immagini da processare

## Licenza

GNU General Public License v3.0