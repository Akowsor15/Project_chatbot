#!/usr/bin/env python
# coding: utf-8

# In[ ]:


---#story
#bot:This is FIFA(Qatar) worldcup 2022. How can we help you? Do you need tickets to any games?
#User: Hi yes please i need tickets/
#Bot: Yes we have tickets available for you. When would you like to see the game?
#User: Tommorrow
#Bot: How many people are going?
#User: 6
#Bot: Which seats would you like to sit in?
#User: Which seats do you have?
#Bot: We have category 1(orange), category 2(red), category 3(green) and category 4(purple), Which category seats would you and your companions like to sit in?
#User: We would like to sit on the top seat category 1 (Orange).
#Bot: Would you like any food and drink to be provided when watching the game?
#User: No thank you.
#Bot:Is that all?
#User: Thats all.
#Bot: For six people that will be £104.
#Bot: Would you like to pay by Card, VISA, PayPal or ApplePay?
#User: VISA
#Bot: Thank you for your VISA payment,Confirmation of booking and infomration regarding the FIFA(Qatar) game will be sent by E=Ticket.
#Bot: Is that all?
#User: Thats all.
#User: Bye.
#stop/


# In[ ]:


---#Domain.yml
 - greet\n",
"  - goodbye\n",
"  - affirm\n",
"  - deny\n",
"  - mood_great\n",
"  - mood_unhappy\n",
"  - bot_challenge\n",
"  - request_tickets\n",
"  - dates_booking\n",
"  - number_people\n",
"  - seats_booking\n",
"  - choice_seats\n",
"  - food\n",
"  - finish\n",
"  - pay_method\n",


# In[ ]:


#config.yml
"  session_expiration_time: 60\n",
"  carry_over_slots_to_new_session: true\n"


# In[ ]:


---#Data/NLU.md
#intent greet
#intent goodbye
#intent affirm
#intent request tickets
#intent date-booking
#intent number of people
#intent seat booking
#intent choice of seat
#intent food intent finish
#intent payment method
#intent deny
#intent mood great
#intent mood unhappy
#intent bot challenge


# In[ ]:


---#Endpoints.yml
#Adding in several features, excellent option for data formmating
# I have added in multiple documents into one single file.


# In[ ]:


---#Credentials.yml
#Encrypted format for passwords, username and for the story line it is the number of people, seat booking and payment option proceedings.


# In[ ]:


{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "Axx1101498",
        "outputId": "62e3695e-5535-476a-Ax213-127a3127e5d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "aksah",
          "text": [
            "Collecting rasa==2.6.2\n",
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "numpy",
                  "prompt_toolkit",
                  "pytz"
                ]
              }
            }
          },
          "metadata": {}
        }
      ],
      "source": [
        "!pip install rasa==2.6.2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Axx1101498"
      },
      "source": [
        "# New section"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "3c52bea6-0ae8-456e-Ax786-c543fe0e059f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
          ]
        }
      ],
      "source": [
        "!python -m spacy download en"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "a759aab3-b5d2-4932-Ax2431-20efc3f35d38"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            
          ]
        }
      ],
      "source": [
        "!pip install nest_asyncio==1.3.3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "1cbcda7e-0796-47ab-AX25431-34e835218a55"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            "event loop ready\n"
          ]
        }
      ],
      "source": [
        "import os \n",
        "import rasa\n",
        "import nest_asyncio\n",
        "\n",
        "nest_asyncio.apply()\n",
        "\n",
        "print(\"event loop ready\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "id": "Axx1101498"
      },
      "outputs": [],
      "source": [
        "from rasa.cli.scaffold import create_initial_project"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "id": "Axx1101498"
      },
      "outputs": [],
      "source": [
        "project = 'test_project'\n",
        "create_initial_project(project)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "1f260d3a-c4f4-4dba-Ax2567-ea5217269002"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['tests',\n",
              " 'actions.py',\n",
              " 'config.yml',\n",
              " 'domain.yml',\n",
              " 'data',\n",
              " '__pycache__',\n",
              " '__init__.py',\n",
              " 'endpoints.yml',\n",
              " 'credentials.yml']"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "os.chdir(project)\n",
        "os.listdir(\".\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "9a1a3864-2253-45d3-ax25674-d8599aa318f5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            "config.yml data/ domain.yml models/\n"
          ]
        }
      ],
      "source": [
        "config = \"config.yml\"\n",
        "training_files = \"data/\"\n",
        "domain = 'domain.yml'\n",
        "output = 'models/'\n",
        "\n",
        "print(config, training_files, domain, output)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "7834e874-ea26-4ab5-axx2221-670988d7dc9c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "axxxx",
          "text": [

          ]
        },
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [

          ]
        },
        {
          "output_type": "stream",
          "name": "axxxx",
          "text": [
            "\n",
            
          ]
        },
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [

          ]
        },
        {
          "output_type": "stream",
          "name": "axxxx",
          "text": [
          ]
        },
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
              
          ]
        }
      ],
      "source": [
        "model_path = rasa.train(domain, config, [training_files], output)\n",
        "print(model_path)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "06ab1a74-c0dd-4af6-A55aXXXX-02f9a1555fc1"
      },
      "outputs": [
        {
          "name": "Aksah",
          "output_type": "stream",
          "text": [
            "Your bot is ready to talk! Type your messages here or send '/stop'.\n",
            "hello\n",
            "\u001b[92mThis is FIFA(Qatar) World Cup 2022, How can we help you? /n Do you need tickets to any games?\u001b[0m\n",
            "Hi yes please i need tickets\n",
            "\u001b[92mYes we have tickets available for you /n when would you like to see the game?\u001b[0m\n",
            "tomorrow\n",
            "\u001b[92mhow many people are going?\u001b[0m\n",
            "6\n",
            "\u001b[92mwhich seats would you like to sit in?\u001b[0m\n",
            "which seats do you have?\n",
            "\u001b[92mWe have category 1(orange), category 2(red), category 3(green) and category 4(purple), /n which category seats would you and your companions like to sit in?\u001b[0m\n",
            "we would like to sit on the top seats category 1(orange)\n",
            "\u001b[92mWould you like any food and drink to be provided when watching the game?\u001b[0m\n",
            "no thank you\n",
            "\u001b[92mIs that all?\u001b[0m\n",
            "thats all\n",
             "\u001b[92mFor six people that will be £104\u001b[0m\n",
            "\u001b[92mwould you like to pay by card, VISA, paypal or apple pay?\u001b[0m\n",
            "VISA\n",
            "\u001b[92mthank you for your VISA payment,confirmation of booking and information regarding the FIFA(Qatar) game will be sent by E-Ticket.\u001b[0m\n",
            "\u001b[92mIs that all?\u001b[0m\n",
            "thats all\n",
            "bye\n",
            "\u001b[92mBye\u001b[0m\n",
            "/stop\n"
          ]
        }
      ],
      "source": [
        "from rasa.jupyter import chat\n",
        "\n",
        "endpoints = 'endpoints.yml'\n",
        "\n",
        "chat(model_path, endpoints)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 312
        },
        "id": "Axx1101498",
        "outputId": "93769238-543f-47c2-Ax21-135a4daded46"
      },
      "outputs": [
        {
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "output_type": "error",
          "traceback": [
            
          ]
        }
      ],
      "source": [
        "chat(model_path, endpoints)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "c474f3AX22-71c2-4318-ab79-94d9c88c3437"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            "Overwriting domain.yml\n"
          ]
        }
      ],
      "source": [
        "%%writefile domain.yml\n",
        "\n",
        "intents:\n",
        "  - greet\n",
        "  - goodbye\n",
        "  - affirm\n",
        "  - deny\n",
        "  - mood_great\n",
        "  - mood_unhappy\n",
        "  - bot_challenge\n",
        "  - request_tickets\n",
        "  - dates_booking\n",
        "  - number_people\n",
        "  - seats_booking\n",
        "  - choice_seats\n",
        "  - food\n",
        "  - finish\n",
        "  - pay_method\n",
        "  \n",
        "\n",
        "responses:\n",
         "  utter_greet:\n",
         "  - text: \"This is FIFA(Qatar) World Cup 2022, How can we help you? /n Do you need tickets to the game? We have got options for you to choose from.\"\n",
         "  - utter_Match:\n",
         "  - text: \"Cat 1\n",
         "  - text: \"Cat 2\n",
         "  - text: \"Cat 3\n",
         "  - text: \"Cat 4\n",
         "  - text: \"Access.\n",
         "  - text: \"Opening match (No 1)\n",
         "  - text: \"£470\n",
         "  - text: \"£334\n",
         "  - text: \"£300\n",
         "  - text: \"£41\n",
         "  - text: \"Group stage (No 2-48)\n",
         "  - text: \"£167\n",
         "  - text: \"£125\n",
         "  - text: \"£52\n",
         "  - text: \"£8\n",
         "  - text: \"Round of 16 (No 49-56)\n",
         "  - text: \"£209\n",
         "  - text: \"£156\n",
         "  - text: \"£73\n",
         "  - text: \"£14\n",
         "  - text: \"Quarter-finals (No 57-60)\n",
         "  - text: \"£324\n",
         "  - text: \"£219\n",
         "  - text: \"£156\n",
         "  - text: \"Semi-finals (No 61-62)\n",
         "  - text: \"£518\n",
         "  - text: \"£501\n",
         "  - text: \"£271\n",
         "  - text: \"£104\n",
         "  - text: \"Third-place match (No 63)\n",
         "  - text: \"£324\n",
         "  - text: \"£229\n",
         "  - text: \"£156\n",
         "  - text: \"£62\n",
         "  - text: \"Final (No 64)\n",
         "  - text: \"£1,223\n",
         "  - text: \"£763\n",
         "  - text: \"£460\n",
         "  - text: \"£156\n",
         "  utter_question:\n",
         "  - text: \"Any thing else i can help you with?\n",
         "  - text: \"E-ticket.\n",
         "  utter_goodbye:\n",
         "  - text: \"Goodbye.\n",
        "  utter_cheer_up:\n",
        "  - text: \"Here is something to cheer you up:\"\n",
        "    image: \"https://i.imgur.com/nGF1K8f.jpg\"\n",
       "\n",
        "  utter_did_that_help:\n",
        "  - text: \"Did that help you?\"\n",
        "\n",
        "  utter_happy:\n",
        "  - text: \"Great, carry on!\"\n",
        "\n",
        "  utter_goodbye:\n",
        "  - text: \"Bye\"\n",
        "\n",
        "  utter_iamabot:\n",
        "  - text: \"I am a bot, powered by Rasa.\"\n",
        "\n",
        "  utter_request_tickets:\n",
        "  - text: \"Yes we have tickets available for you /n when would you like to see the game?\"\n",
        "  \n",
        "  utter_dates_booking:\n",
        "  - text: \"how many people are going?\"\n",
        "\n",
        "  utter_number_people:\n",
        "\n",
        "  - text: \"which seats would you like to sit in?\"\n",
        "\n",
        "  utter_seats_booking:\n",
        "  utter_booking_for_match_date:\n",
        "  type section:\n",
        "  text: \"Book a time for your match-date:\n",
        "  type: \"mrkdown:\n",
        "  accessory:\n",
        "  type: datepicker:\n",
        "  initial_date: 18-12-2022:\n",
        "  placeholder:\n",
        "  type: plain_text:\n",
        "  text: Select a date\n",
        "\n",
        "  - text: \"We have category1(orange),category2(red), category3(green) and category4(purple) /n which ones would you like to sit in?\"\n",
        "\n",
        "  utter_choice_seats:\n",
        "\n",
        "  - text: \"Would you like any food and drink to be provided when watching the game?\"\n",
        "\n",
        "  utter_food:\n",
        "\n",
        "  - text: \"Is that all?\"\n",
        "\n",
        "  utter_finish: \n",
        "\n",
        "  - text: \"would you like to pay by card, VISA, paypal or apple pay?\"\n",
        "\n",
        "  utter_pay_method:\n",
        "\n",
        "  - text: \"thank you for your payment, have a good day\"\n",
        "\n",
        "session_config:\n",
        "  session_expiration_time: 60\n",
        "  carry_over_slots_to_new_session: true\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "029d71cb-8200-axx221-86b4-b6565189ebef"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            "Overwriting data/nlu.md\n"
          ]
        }
      ],
      "source": [
        "%%writefile data/nlu.md\n",
        "\n",
        "## intent:greet\n",
        "- hey\n",
        "- hello\n",
        "- hi\n",
        "- good morning\n",
        "- good evening\n",
        "- hey there\n",
        "\n",
        "## intent:goodbye\n",
        "- bye\n",
        "- goodbye\n",
        "- see you around\n",
        "- see you later\n",
        "\n",
        "## intent:affirm\n",
        "- yes\n",
        "- indeed\n",
        "- of course\n",
        "- that sounds good\n",
        "- correct\n",
        "\n",
        "## intent: request_tickets\n",
        "\n",
        "- yes I need tickets to a game\n",
        "- I want tickets to the latest game\n",
        "- I need tickets\n",
        "- yes please I need tickets\n",
        "- I need some tickets for the new game\n",
        "\n",
        "## intent: dates_booking\n",
        "\n",
        "- tomorrow\n",
        "- today\n",
        "- next week\n",
        "- Monday\n",
        "- Tuesday\n",
        "- Wednesday\n",
        "- Thursday\n",
        "- Friday\n",
        "- Saturday\n",
        "- Sunday\n",
        "- Next Month\n",
        "\n",
        "## intent: number_people\n",
        "\n",
        "- 1\n",
        "- 2 \n",
        "- 3 \n",
        "- 4\n",
        "- 5 \n",
        "- 6 \n",
        "- 7\n",
        "- 8 \n",
        "- 9 \n",
        "- 10\n",
        "\n",
        "## intent: seats_booking\n",
        "- which seats do you have?\n",
        "- what are the seat arrangements?\n",
        "- what seats are currently available?\n",
        "- which colour category seats are the best viewing seats to watch the football game?\n",
        "- orange\n",
        "- red \n",
        "- green\n",
        "- purple\n",
        "\n",
        "## intent: choice_seats\n",
        "\n",
        "- we would like to sit at the top orange seats\n",
        "- we would like to sit at the middle red seats\n",
        "- we would like to sit at the next middle green seats\n",
        "- we would like to sit at the bottom purple seats\n",
        "- top orange seats\n",
        "- middle red seats\n",
        "- next middle green seats\n",
        "- bottom purple seats\n",
        "\n",
        "## intent: food\n",
        "\n",
        "- no \n",
        "- no we dont need any food or drink\n",
        "- no thank you\n",
        "- yes\n",
        "- yes we would like to have food and drink\n",
        "- yes please\n",
        "\n",
        "##intent: finish\n",
        " \n",
        "- yes \n",
        "- yes thats all\n",
        "- yes please\n",
        "\n",
        "##intent: pay_method\n",
        "\n",
        "- apple pay\n",
        "- paypal\n",
        "- card\n",
        "- VISA\n",
        "\n",
        "##intent: Good_Bye\n",
        "\n",
        "- goodbye\n",
        "- thanks for your time\n",
        "- thank you\n",
        "- cheers\n",
        "- thanks a lot\n",
        "- thanks\n",
        "\n",
        "\n",
        "## intent:deny\n",
        "- no\n",
        "- never\n",
        "- I don't think so\n",
        "- don't like that\n",
        "- no way\n",
        "- not really\n",
        "\n",
        "## intent:mood_great\n",
        "- perfect\n",
        "- very good\n",
        "- great\n",
        "- amazing\n",
        "- wonderful\n",
        "- I am feeling very good\n",
        "- I am great\n",
        "- I'm good\n",
        "\n",
        "## intent:mood_unhappy\n",
        "- sad\n",
        "- very sad\n",
        "- unhappy\n",
        "- bad\n",
        "- very bad\n",
        "- awful\n",
        "- terrible\n",
        "- not very good\n",
        "- extremely sad\n",
        "- so sad\n",
        "\n",
        "## intent:bot_challenge\n",
        "- are you a human?\n",
        "- am I talking to a human?\n"
        "- are you a bot?\n",
        "- am I talking to a bot?\n",
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Axx1101498",
        "outputId": "9f1fa1d2-ada6-4395-22356-957e08b76001"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "Aksah",
          "text": [
            "Overwriting data/stories.md\n"
          ]
        }
      ],
      "source": [
        "%%writefile data/stories.md\n",
        "\n",
        "## happy path\n",
        "* greet\n",
        "  - utter_greet\n",
        "* mood_great\n",
        "  - utter_happy\n",
        "\n",
        "## sad path 1\n",
        "* greet\n",
        "  - utter_greet\n",
        "* mood_unhappy\n",
        "  - utter_cheer_up\n",
        "  - utter_did_that_help\n",
        "* affirm\n",
        "  - utter_happy\n",
        "\n",
        "## sad path 2\n",
        "* greet\n",
        "  - utter_greet\n",
        "* mood_unhappy\n",
        "  - utter_cheer_up\n",
        "  - utter_did_that_help\n",
        "* deny\n",
        "  - utter_goodbye\n",
        "\n",
        "## say goodbye\n",
        "* goodbye\n",
        "  - utter_goodbye\n",
        "\n",
        "## bot challenge\n",
        "* bot_challenge\n",
        "  - utter_iamabot\n",
        "\n",
        "## request tickets\n",
        "\n",
        "* request_tickets\n",
        "  - utter_request_tickets\n",
        "\n",
        "## dates booking\n",
        "\n",
        "* dates_booking\n",
        "  - utter_dates_booking\n",
        "\n",
        "## number people\n",
        "* number_people\n",
        "  - utter_number_people\n",
        "\n",
        "## seats_booking\n",
        "* seats_booking\n",
        " - utter_seats_booking\n",
        "\n",
        "## choice_seats\n",
        "* choice_seats\n",
        " - utter_choice_seats\n",
        "\n",
        "## food\n",
        "* food\n",
        " - utter_food\n",
        "\n",
        "## finish\n",
        "* finish\n",
        " - utter_finish\n",
        "\n",
        "## pay_method\n",
        "* pay_method\n",
        " - utter_pay_method"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "id": "Axx1101498"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3.11",
      "name": "python 3.11"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}

