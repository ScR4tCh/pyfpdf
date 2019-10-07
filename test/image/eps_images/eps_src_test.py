"""png_image_test.py"""

import unittest
import sys
import os
sys.path.insert(0,
  os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.path.join('..', '..', '..')
  )
)

import fpdf
import test
from test.utilities import relative_path_to, \
                           set_doc_date_0, \
                           calculate_hash_of_file

class InsertEPS(unittest.TestCase):
  def test_insert_png_files(self):
    pdf = fpdf.FPDF(unit = 'pt')
    pdf.compress = False

    images = [relative_path_to(f) for f
              in os.listdir(relative_path_to('.'))
              if f.endswith(".eps") or f.endswith(".ai")]
    images.sort()

    for image in images:
        pdf.add_page()
        with open(image) as img:
          pdf.eps(img.read(), x=0, y=0, w=0, h=0, link=None)

    set_doc_date_0(pdf)
    outfile = relative_path_to('insert_eps_test.pdf')
    pdf.output(outfile, 'F')
    # print(calculate_hash_of_file(outfile))

    test_hash = calculate_hash_of_file(outfile)
    # ordered the images for reproduceability
    #self.assertEqual(test_hash, "0085260bea512b9394ce1502b196240a")

    # self.assertEqual(test_hash, "4f65582566414202a12ed86134de10a7")
    #os.unlink(outfile)

if __name__ == '__main__':
  # http://stackoverflow.com/questions/9502516/how-to-know-time-spent-on-each-
  # test-when-using-unittest
  import time
  @classmethod
  def setUpClass(cls):
      cls.start_ = time.time()

  @classmethod
  def tearDownClass(cls):
      t = time.time()
      print("\n%s.%s: %.3f" % (cls.__module__, cls.__name__, t - cls.start_))

  unittest.TestCase.setUpClass = setUpClass
  unittest.TestCase.tearDownClass = tearDownClass

  unittest.main()

## Code used to create test: Test created in place
