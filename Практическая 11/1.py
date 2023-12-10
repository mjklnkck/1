import tkinter as tk
import requests
import json

def parse(repo, label):
    file = f'{repo}_output.json'
    try:
        output = requests.get(f'https://api.github.com/users/{repo}')
        output.raise_for_status()  # Raises an HTTPError if the request was unsuccessful
        user_data = output.json()
        filtered_data = {key: user_data[key] for key in user_data if key in ['company', 'created_at', 'email', 'id', 'name', 'url']}
        with open(file, 'w') as file_write:
            json.dump(filtered_data, file_write, indent=4)
        message = f'Информация сохранена в {file}'
    except requests.exceptions.RequestException as err:
        message = f'Ошибка при отправке запроса: {err}'
    except json.JSONDecodeError as err:
        message = f'Ошибка при обработке JSON: {err}'
    except KeyError as err:
        message = f'Отсутствует ожидаемое поле в ответе: {err}'
    except Exception as err:
        message = f'Произошла ошибка: {err}'
    label.config(text=message)

def main():
    window = tk.Tk()
    window.title('GitHub json parser')

    repo_label = tk.Label(window, text='Введите имя репозитория:')
    repo_entry = tk.Entry(window)
    parse_btn = tk.Button(window, text='Parse', command=lambda: parse(repo_entry.get(), output_label))
    output_label = tk.Label(window, foreground='blue')

    modules = [repo_label, repo_entry, parse_btn, output_label]

    for module in modules:
        module.pack(pady=10)

    window.mainloop()

main()