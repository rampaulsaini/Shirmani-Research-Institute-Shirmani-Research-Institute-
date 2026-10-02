from factory.supreme_nlp_benchmark import evaluate

def main():
    rows=[
      {"expected":"positive-pattern","predicted":"positive-pattern","confidence":.9,"correct":True},
      {"expected":"negative-pattern","predicted":"negative-pattern","confidence":.9,"correct":True},
      {"expected":"neutral-or-uncertain","predicted":"positive-pattern","confidence":.8,"correct":False},
    ]
    m=evaluate(rows)
    assert 0 <= m["accuracy"] <= 1
    assert 0 <= m["macro_precision"] <= 1
    assert 0 <= m["macro_recall"] <= 1
    assert 0 <= m["macro_f1"] <= 1
    assert 0 <= m["expected_calibration_error"] <= 1
    print("SUPREME_NLP_BENCHMARK_CONTRACT: PASS")

if __name__=="__main__": main()
