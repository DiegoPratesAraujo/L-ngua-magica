from flask import Flask, render_template, request
import tradutor_magico

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  magic_text = ""
  phonemes = ""
  process_description = ""
  latin_text = ""
  if request.method == 'POST':
    if 'input_text_latim' in request.form:
      text = request.form.get('input_text_latim')
      magic_text, phonemes, process_description = tradutor_magico.latim_para_magico(
        text)
    elif 'input_text_magico' in request.form:
      text = request.form.get('input_text_magico')
      latin_text, process_description = tradutor_magico.magico_para_latim(text)

  return render_template('index.html',
                         magic_text=magic_text,
                         phonemes=phonemes,
                         process_description=process_description,
                         latin_text=latin_text)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
