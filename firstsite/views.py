# User created file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('''<h1>Hello World</h1> 
                            <a href="https://www.orgzit.com"> Orgzit </a>
                            <br>
                            <br>
                            <a href="/about"> About </a>
                            <br>
                            <br>
                            <a href="/opentextfile"> Text File </a>
                            <br>
                            <br>
                            <a href="/indexrender"> Index file render </a>
                            <br>
                            <br>
                            <a href="/textanalyzer"> Text Analyzer </a>
                        ''')


def about(request):
    return HttpResponse('''This is an about page
                        <br>
                        <a href="/"> Back </a>
                        ''')


def opentextfile(request):
    with open("E:\\Users\\arora\\PycharmProjects\\DjangoProject\\firstsite\\firstsite\\text1.txt", "r") as f:
        content = f.read()
    return HttpResponse(
        f'''{content}
                        <br>
                        <a href="/"> Back </a>''')


def indexrender(request):
    params = {
        "name": "Shreyansh",
        "place": "Delhi"
    }
    return render(request, 'index.html', params)


def textanalyzer(request):
    return render(request, 'index2.html')


def manipulate_text(request):
    # Get the text
    entered_text = request.POST.get('text', 'default')

    # Checkbox values
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    count_char = request.POST.get('count_char', 'off')

    punctuations = '''!()?.,;:<>/'"-[]{}#$^&'''

    final_string = '' if remove_punc == 'on' else entered_text
    purpose = []
    if remove_punc == 'on':
        purpose += ['Removed punctutaions']
        for char in entered_text:
            if char not in punctuations:
                final_string += char

    if full_caps == 'on':
        purpose += ['FULL CAPITALIZE']
        final_string = final_string.upper()

    print(len(final_string))

    if extra_space_remover == 'on':
        final_string2 = ''
        purpose += ['Removed Extra Space']
        for idx, char in enumerate(final_string):
            if len(final_string) - 1 > idx and (not (final_string[idx] == ' ' and final_string[idx + 1] == ' ')):
                final_string2 += final_string[idx]
        final_string = final_string2

    if new_line_remover == 'on':
        final_string3 = ''
        purpose += ['Removed New Lines']
        for char in final_string:
            if char != '\n' and char != '\r':
                final_string3 += char
        final_string = final_string3

    length = None
    if count_char == 'on':
        length = len(final_string)

    params = {
        'purpose': purpose,
        'analyzed_text': final_string,
        'length': length
    }
    return render(request, 'analyze.html', params)
