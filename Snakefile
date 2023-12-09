rule prepare:
    output:
        "./data/Index",
        "./data/wine.data",
        "./data/wine.names"
    shell:
        "python3 prepare_data.py"
rule profile:
    input:
        "./data/wine.data"
    output:
        "./profiling/report.html",
        "./data/wine.csv"
    shell:
        "python3 profile.py"
rule analyze:
    input:
        "./data/wine.csv"
    output:
        "./results/classification_report.txt",
        "./results/confusion_matrix.txt",
        "./results/correlation_heatmap.png",
        "./results/summary_statistics.csv"

    shell:
        "python3 analyze.py"