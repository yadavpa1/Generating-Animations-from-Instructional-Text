# Generating-Animations-from-Instructional-Text

This is the code for [Generating Animations from Instructional Text](https://www.researchgate.net/publication/342740629_Generating_Animations_from_Instructional_Text).

Generating animations from text finds application in numerous areas like screenplay writing, instructional videos, public safety, and video user manuals, etc. However, translating natural language text into animations is a challenging task. We develop a text-to-animation system that can handle any simple instructional text. We have created an NLP pipeline to extract action sequences from cooking recipes and map them to appropriate atomic actions present in the system’s knowledge base. This paper explores a novel approach of linking Graphics with Natural Language Processing (NLP). Our goal is to obviate the necessity of having a large collection of stored graphics.

## Usage

Install all the pip modules in requirements.txt in nlp_pipeline_server directory. Note: cython and numpy should be installed before benepar

Create a virtualenv with python3
```
virtualenv env1 --python=python3
```

Run below command to start the nlp pipeline server
```
./nlp_pipeLine_server/run_server.sh
```

## Citation
If this code is useful for your research, do cite:
```
@article{yadav2020generating,
  title={Generating Animations from Instructional Text},
  author={Yadav, Pooja and Sathe, Kaivalya and Chandak, Manoj},
  journal={International Journal},
  volume={9},
  number={3},
  year={2020}
}
```
