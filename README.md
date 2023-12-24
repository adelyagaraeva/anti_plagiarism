<h2 align="center">
    <img src="https://github.com/adelyagaraeva/anti_plagiarism/assets/146413113/262ae88c-b239-4ffd-b840-02ea78c13411" height="128px" width="128px">
</h2>

<p align="center">
    <img src="https://img.shields.io/badge/python-3.7+-green">
    <img src="https://img.shields.io/badge/license-MIT-green">
</p>

# anti_plagiarism
## Описание проекта:


Мы реализовали проект для определения степени похожести кодов и текстов и выявления академического плагиата.
Запуск скрипта будет осуществляться через командную строку. Программа на вход получает два файла на языке python или папку с файлами для сравнения. При запуске есть возможность выбрать метрику, используемую для вычисления вероятности плагиата. Пользователю доступны: расстояние Левенштейна, Дамерау-Левенштейна и Джаро-Винкера.

Исходные файлы в нашей программе представляются в виде абстрактных синтаксических деревьев. С помошью этих метрик и определяется расстояние между ними.

Программа выводит число от 0 до 1, которое имеет смысл вероятности или абсолютное значение выбранной метрики.

Для удобства мы реализовали веб-интерфейс, который позволит даже людям, далеким от сферы программирования,использовать нану систему антиплагиата.


## Как запускать:
Чтобы получить вывод в консоль: path_to_the_first_file path_to_the_second_file -m metric_name 
                                path_to_folder -m metric_name 
Вывод в файл с расширением csv: path_to_the_first_file path_to_the_second_file -m metric name -pandas path_to_resul_file
                                path_to_folder -m metric name -pandas path_to_resul_file
запуск приложения из консоли:   streamlit run path_to_file
