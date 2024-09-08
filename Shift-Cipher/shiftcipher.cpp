#include <iostream>
using namespace std;

string enkripsi(string text, int n)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
        {
            result += char((int(text[i] + n - 65) % 26 + 26) % 26 + 65);
        }
        else if (islower(text[i]))
        {
            result += char((int(text[i] + n - 97) % 26 + 26) % 26 + 97);
        }
        else
        {
            result += text[i];
        }
    }
    return result;
}

string dekripsi(string text, int n)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
        {
            result += char((int(text[i] - n - 65) % 26 + 26) % 26 + 65);
        }
        else if (islower(text[i]))
        {
            result += char((int(text[i] - n - 97) % 26 + 26) % 26 + 97);
        }
        else
        {
            result += text[i];
        }
    }
    return result;
}

void menu()
{
    string text;
    int n, operasi;
    cout << "masukkan teks : ";
    getline(cin, text);
    cout << "masukkan n (nilai pergeseran) : ";
    cin >> n;
    cout << "1. enkripsi\n";
    cout << "2. dekripsi\n";
    cout << "pilih operasi : ";
    cin >> operasi;
    switch (operasi)
    {
    case 1:
        cout << "hasil enkripsi : " << enkripsi(text, n) << '\n';
        break;
    case 2:
        cout << "hasil dekripsi : " << dekripsi(text, n) << '\n';
        break;
    default:
        cout << "operasi tidak sesuai, keluar program";
        exit(0);
    }
}

int main()
{
    menu();
}