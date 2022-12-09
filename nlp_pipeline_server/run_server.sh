if [ ! -f ./.first_time_install ]; then
    touch .first_time_install
    echo ".first_time_install created"
    python -m spacy download en
    echo "python -m spacy download en finished"
    python first_time_install.py
    echo "python first_time_install.py finished"
    #echo "File not found!"
fi

python extractor.py
