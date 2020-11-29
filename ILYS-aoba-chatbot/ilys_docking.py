import sys
import logging
import argparse
from os import path
from typing import List
from pprint import pprint

from neural_dialogue_model.model_args import Args
from neural_dialogue_model.models import NeuralDialogueModel


logging.basicConfig(
    format='%(asctime)s #%(lineno)s %(levelname)s %(name)s :::  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

MODEL='/work02/miyawaki/ILYS-aoba-chatbot/models/ilys_aoba_transformer_finetuned.pt'
SPM='/work02/miyawaki/ILYS-aoba-chatbot/models/spm_10M_tweets.cr9999.bpe.32000.model'
VOCAB='/work02/miyawaki/ILYS-aoba-chatbot/fairseq_vocab'

def create_parser():
    parser = argparse.ArgumentParser(description='')
    group = parser.add_argument_group("Dialogues")
    group.add_argument(
        '--model', 
        type=path.abspath, 
        metavar="FP", 
        default=MODEL,
        help="Path to model parameters"
    )
    group.add_argument(
        '--spm', 
        type=path.abspath, 
        metavar="FP", 
        default=SPM,
        help="Path to sentencepiece model"
    )
    group.add_argument(
        '--vocab', 
        type=path.abspath, 
        metavar="FP", 
        default=VOCAB,
        help="Path to vocab"
    )
    return parser


def docking(context:str, previous_contexts:List[str]=[]) -> str:
    previous_contexts.append(context)
    responses = model(contexts)
    previous_contexts.append(responses[0])
    return responses[0]


if __name__ == '__main__':
    parser = create_parser()
    parser_args = parser.parse_args()

    args = Args(
        model_path=parser_args.model, 
        spm_path=parser_args.spm, 
        vocab_path=parser_args.vocab
    )

    model = NeuralDialogueModel(args)

    contexts, count = [], 0
    while True:
        try:
            context = input("\033[32m" + f"In [{count}]: " + "\033[0m")
            response = docking(context, contexts)
            print("\033[32m" + f"Out[{count}]: " + "\033[0m", response)
            pprint(contexts)
            count += 1
            print()
        except KeyboardInterrupt:
            break
