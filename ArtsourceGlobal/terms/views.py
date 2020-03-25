from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def terms1(request):
    return render(request, 'terms/terms1.html')


# for small file download
# with open('file_name.txt') as f:
#
#     c = f.read()
#
#   return HttpResponse(c)


# for large file download
# from django.http import StreamingHttpResponse

# def big_file_download(request):
#     # do something...
#
#     def file_iterator(file_name, chunk_size=512):
#
#         with open(file_name) as f:
#
#             while True:
#
#                 c = f.read(chunk_size)
#
#                 if c:
#
#                     yield c
#
#                 else:
#
#                     break
#
#     the_file_name = "big_file.pdf"
#
#     response = StreamingHttpResponse(file_iterator(the_file_name))
#
#     response['Content-Type'] = 'application/octet-stream'
#
#     response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
#
#     return response


# use reportlab api to output pdf: pip install reportlab

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
#
# def some_view(request):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()
#
#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#
#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')