from fastapi import FastAPI, UploadFile, File
from Visualizations import check_code_quality, create_histogram, create_pie_chart, create_bar_chart
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/analyze/")
async def analyze_code(source_code: str):
    """
    ניתוח קוד ומייצר גרפים בהתאם לבעיות שמזוהות.
    """
    function_lengths, warnings_count = check_code_quality(source_code)

    create_histogram(function_lengths)
    create_pie_chart(warnings_count)
    create_bar_chart(warnings_count)

    return {
        "histogram": "histogram.png",
        "pie_chart": "pie_chart.png",
        "bar_chart": "bar_chart.png"
    }

@app.get("/download/{filename}")
async def download_file(filename: str):
    """
    מאפשר להוריד קבצים שנשמרו.
    """
    return FileResponse(filename)
