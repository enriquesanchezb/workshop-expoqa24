import logging

from langchain.evaluation.criteria import LabeledCriteriaEvalChain
from langchain_community.llms import Ollama

from prompt.summary import prompt
from src.summarize import summarize

logger = logging.getLogger(__name__)

criteria = {
    "language": "The output should be in English.",
    "clarity": "Are the sentences clear and easy to understand?",
    "precision": "Is the writing precise, with no unnecessary words or details?",
    "truthfulness": "Does the writing feel honest and sincere?",
    "relevance": "The output should be relevant to the prompt.",
    "accuracy": "The output should be accurate.",
}

criteria_output = {
    "response-output": "The output should be as is described in the prompt.",
    "size": "The output should be of a reasonable size as described in the prompt, if only one sentence is expected, the output should be one sentence, if only one word is expected, the output should be one word.",
    "relevance": "The output should be relevant to the prompt.",
    "accuracy": "The output should be accurate.",
}


def test_summarize_answer_lenght():
    text = """
    Let's explore the concept of urban gardening, an increasingly popular practice that transforms city landscapes and fosters community engagement. Urban gardening involves cultivating plants and vegetables in densely populated urban areas, utilizing rooftops, balconies, vacant lots, and even window sills. This movement not only beautifies the city but also provides fresh produce to residents who might otherwise lack access to green spaces and healthy foods.
    The benefits of urban gardening extend beyond aesthetics and nutrition. It promotes environmental responsibility by reducing the urban heat island effect and improving air quality. Green spaces help absorb rainwater, reducing the risk of flooding, and they also sequester carbon, combating urban pollution. Moreover, these gardens create habitats for urban wildlife, supporting biodiversity.Community gardens serve as social hubs where people of diverse backgrounds can connect, share knowledge, and collaborate. They provide educational opportunities for children and adults alike, teaching valuable skills such as composting, planting, and sustainable living. In essence, urban gardening is not just about growing plants—it's about cultivating healthier, more vibrant urban communities. Through these small patches of greenery, city dwellers can reconnect with nature and each other, enhancing the quality of urban life.
    """

    summary = summarize(text)
    word_count = len(summary.split())
    assert word_count <= 50


def test_summarize_answer_accuracy():
    text = """
    Let's explore the concept of urban gardening, an increasingly popular practice that transforms city landscapes and fosters community engagement. Urban gardening involves cultivating plants and vegetables in densely populated urban areas, utilizing rooftops, balconies, vacant lots, and even window sills. This movement not only beautifies the city but also provides fresh produce to residents who might otherwise lack access to green spaces and healthy foods.
    The benefits of urban gardening extend beyond aesthetics and nutrition. It promotes environmental responsibility by reducing the urban heat island effect and improving air quality. Green spaces help absorb rainwater, reducing the risk of flooding, and they also sequester carbon, combating urban pollution. Moreover, these gardens create habitats for urban wildlife, supporting biodiversity.Community gardens serve as social hubs where people of diverse backgrounds can connect, share knowledge, and collaborate. They provide educational opportunities for children and adults alike, teaching valuable skills such as composting, planting, and sustainable living. In essence, urban gardening is not just about growing plants—it's about cultivating healthier, more vibrant urban communities. Through these small patches of greenery, city dwellers can reconnect with nature and each other, enhancing the quality of urban life.
    """

    summary = summarize(text)

    llm_verifier = Ollama(model="phi3")
    evaluator = LabeledCriteriaEvalChain.from_llm(llm=llm_verifier, criteria=criteria)
    result_relevance = evaluator.evaluate_strings(
        prediction=summary, reference=prompt, input=text
    )
    logger.info("result_relevance: %s", result_relevance)
    assert result_relevance["score"] == 1, result_relevance
