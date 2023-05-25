{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNQ/WDPMmT1NjzmUZqVgrZ7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hyeontae04/202310968/blob/main/hw10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z49jQqF5zSyU"
      },
      "outputs": [],
      "source": [
        "import pickle\n",
        "filename = 'score.bin'\n",
        "\n",
        "def input_scores():\n",
        "  s = []\n",
        "  i = 1\n",
        "  while (True) :\n",
        "    n = int(input(f'#{i}?'))\n",
        "    if n < 0:\n",
        "      break\n",
        "    s.append(n)\n",
        "    i += 1\n",
        "  return s\n",
        "\n",
        "def get_average(s) :\n",
        "  total = 0 \n",
        "  for n in s :\n",
        "    total += n\n",
        "  return total / len(s) \n",
        "\n",
        "def show_scores(s):\n",
        "  for n in s:\n",
        "    print(n, end= ' ')\n",
        "  print()\n",
        "def save_data(sbag, filepath):\n",
        "  with open(filepath, 'w', encoding='utf8')as file:\n",
        "    for item in sbag:\n",
        "      file.write(f'{item}Wn')\n",
        "\n",
        "def load_data(filepath) :\n",
        "  lines = []\n",
        "  with open(filepath, 'r', encoding='utf8')as file:\n",
        "    for line in file:\n",
        "      lines.append(line.strip())\n",
        "  return lines\n",
        "\n",
        "#주프로그램부 \n",
        "if os.path.exists(filename):\n",
        "  print('[파일 읽기]')\n",
        "  scores = load_data(filename)\n",
        "  show(scores)\n",
        "else:\n",
        "  shopping_bag = []\n",
        "while True:\n",
        "  if add(scores) == False:\n",
        "    break\n",
        "show(scores)\n",
        "save_data(scores, filename)\n",
        "\n",
        "\n",
        "\n",
        "  #주프로그램부\n",
        "print('[점수 입력]')\n",
        "scores = input_scores()\n",
        "print('Wn[점수 출력]')\n",
        "print('개인 점수: ', end= '')\n",
        "show_scores(scores)\n",
        "avg = get_average(scores)\n",
        "print(f'평균: {avg:.1f}')"
      ]
    }
  ]
}