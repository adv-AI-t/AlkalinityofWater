from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        volWater = float(request.form['volWater'])
        normality = float(request.form['normality'])
        #logic of the process
        ppt = float(request.form['ppt'])
        mpt = float(request.form['mpt'])
        p = (ppt * normality * 50 * 1000) / volWater
        m = (mpt * normality * 50 * 1000) / volWater
        half_M = m / 2

        res2=round(2*p,2)
        res3=round(m,2)
        res4=round(m-(2*p),2)
        res5=round((2*p)-m,2)
        res6=round((2*m)-(2*p))

        if volWater>0 and normality>0 and ppt>=0 and mpt>=0 and mpt>=ppt:
            if p == 0:
                return f'''<html>
                                            <body>
                                            <font style="font-family:Arial">
                                            <h3>Bicarbonate alkalinity present
                                            <br>
                                            <i>As P = 0,</i><br>
                                            [HCO<sub>3</sub><sup>-</sup> ] = {res3} ppm
                                            </h3>
                                            <br>

                                            <a href="https://joshiadvait.pythonanywhere.com">Check for other values</a>
                                            </body>
                                            </html>
                                        '''
            elif p == half_M:
                return f'''<html>
                                            <body>
                                            <font style="font-family:Arial">
                                            <h3>Carbonate alkalinity present
                                            <br>
                                            <i>As P = M/2,</i><br>
                                            [CO<sub>3</sub><sup>2-</sup> ] = {res3} ppm
                                            </h3>
                                            <br>

                                            <a href="https://joshiadvait.pythonanywhere.com">Check for other values</a>
                                            </body>
                                            </html>
                                        '''
            elif p == m:
                return f'''<html>
                                            <body>
                                            <font style="font-family:Arial">
                                            <h3>Hydroxide alkalinity present
                                            <br>
                                            <i>As P = M,</i><br>
                                            [OH<sup>-</sup> ] = {res3} ppm
                                            </h3>
                                            <br>

                                            <a href="https://joshiadvait.pythonanywhere.com">Check for other values</a>
                                            </body>
                                            </html>
                                        '''
            elif p < half_M:
                return f'''<html>
                                            <body>
                                            <font style="font-family:Arial">
                                            <h3>Carbonate and Bicarbonate alkalinity present
                                            <br>
                                            <i>As P &lt; M/2,</i><br>
                                            [CO<sub>3</sub><sup>2-</sup> ] = {res2} ppm
                                            <br>
                                            [HCO<sub>3</sub><sup>-</sup> ] = {res4} ppm
                                            </h3>
                                            <br>

                                            <a href="https://joshiadvait.pythonanywhere.com">Check for other values</a>
                                            </body>
                                            </html>
                                        '''
            else:
                return f'''<html>
                            <body>
                            <font style="font-family:Arial">
                            <h3>Hydroxide and Carbonate alkalinity present
                            <br>
                            <i>As P &gt; M/2,</i><br>
                            [OH<sup>-</sup> ] = {res5} ppm
                            <br>
                            [CO<sub>3</sub><sup>2-</sup> ] = {res6} ppm
                            </h3>
                            <br>

                            <a href="https://joshiadvait.pythonanywhere.com">Check for other values</a>
                            </body>
                            </html>
                        '''
        else:
            return f'''<html>
                        <body>

                        Invalid input!<br><br>
                        <a href="https://joshiadvait.pythonanywhere.com">Try again</a>
                        </body>
                        <html>
                        '''

    else:
        #front end of form + theory
        return '''

            <form method="post">
            <head>
            <title>Alkalinity of water</title>
            </head>
            <body>
            <style>
            input[type=submit]
            {
              background-color: #32C067;
              border: none;
              color: white;
              padding: 8px 16px;
              text-decoration: none;
              margin: 2px 1px;
              cursor: pointer;

            }
            table,
            th,
            td
            {
                padding: 5px;
                border: 1px solid black;
                border-collapse: collapse;

            }

            </style>
            <font style="font-family:Arial" size="3">
            <h1><center><font color = "148782">Alkalinity of Water</font></center></h1>
            <h2>
            Aim:</h2> To determine alkalinity of given water sample
            <br>
            <h2>
            Apparatus:</h2> Water sample, Acid of known normality, Phenolphthalein, Methyl Orange, Conical flask, Burette
            <br><h2>
            Theory:
            <br></h2>
            <b>Phenolphthalein Alkalinity</b><br>
            Initially, Phenolphthalein indicator is added to the water sample.<br>Then, titration is carried out. End point is marked by color change from <font color="D850FF"><b>pink</b></font> to colorless.
            <br>At this point, all OH<sup>-</sup> ions are neutralized and half of the CO<sub>3</sub><sup>2-</sup> ions are neutralized or it can be said that all the CO<sub>3</sub><sup>2-</sup> ions get converted into HCO<sub>3</sub><sup>-</sup> ions.
            <br><br><b>Methyl Orange Alkalinity</b><br>
            In the second part of titration, HCO<sub>3</sub><sup>-</sup> ions undergo neutralization.<br>
            There are two types of HCO<sub>3</sub><sup>-</sup> ions: some are present from beginning and some are formed by half neutralization of CO<sub>3</sub><sup>2-</sup> ions.
            <br>Methyl orange indicator gives <font color="FF7F2C"><b>orange</b></font> color at the end point from <font color="#F3D060"><b>yellow</b></font> color, which is obtained at pH 4.5
            <br>Methyl endpoint indicates neutralization of all the HCO<sub>3</sub><sup>-</sup> ions.
            <br><br>
            <u>Standard notations for various values:</u><br>
            <b>V</b> = Volume of water sample<br>
            <b>V1</b> = Volume of acid upto P end point<br>
            <b>V2</b> = Volume of acid upto M end point<br>
            <b>N</b> = Normality of acid
            <br><br>
            Formulae to calculate P and M:
            <br>
            <i><b>P = (V1/V) &#215; N &#215; 50 &#215; 1000
            <br>
            M = (V2/V) &#215; N &#215; 50 &#215; 1000</i></b>
            <br><br>
            Following is the table from which inference can be obtained:
            <br><br>
            <table>
            <tr>
            <td></td>
            <td><b>[OH<sup>-</sup> ]</b></td>
            <td><b>[CO<sub>3</sub><sup>2-</sup> ]</b></td>
            <td><b>[HCO<sub>3</sub><sup>-</sup> ]</b></td>
            </tr>
            <tr>
            <td><b>P=0</b></td>
            <td>0</td>
            <td>0</td>
            <td>M</td>
            </tr>
            <tr>
            <td><b>P=M/2</b></td>
            <td>0</td>
            <td>2P</td>
            <td>0</td>
            </tr>
            <tr>
            <td><b>P=M</b></td>
            <td>M</td>
            <td>0</td>
            <td>0</td>
            </tr>
            <tr>
            <td><b>P&lt;M/2</b></td>
            <td>0</td>
            <td>2P</td>
            <td>M-2P</td>
            </tr>
            <tr>
            <td><b>P&gt;M/2</b></td>
            <td>2P-M</td>
            <td>2(M-P)</td>
            <td>0</td>
            </tr>
            </table>
            <h2>Enter details:</h2></font>
            <font style="font-family:Arial">
            <table>

            <tr>
            <td>
              <label for="volWater">Enter volume of water sample (V in ml):</label>
            </td>
            <td>
              <input type="number" id="volWater" name="volWater" required>
            </td>
            </tr>
            <tr>
            <td>
              <label for="normality">Enter Normality of acid (N):</label>
            </td>
            <td>
              <input type="number" id="normality" name="normality" step="0.001" required>
            </td>
            </tr>
            <tr>
            <td>
                <label for="ppt"><font color="D850FF">Volume of acid upto P end point (in ml): </font></label>
            </td>
            <td>
              <input type="number" id="ppt" name="ppt" step="0.1"required>
            </td>
            </tr>
            <tr>
            <td>
              <label for="mpt"><font color="FF7F2C">Volume of acid upto M end point (in ml): </font></label>
            </td>
            <td>
              <input type="number" id="mpt" name="mpt" step="0.1"required>
            </td>
            </tr>
            </table>
              <br>
              <input type="submit" value="Check result">
            </font>
            </form>

            <br><br>
            <font style="font-family:Arial">
            <b>Guided by:</b><br><br>
            Mr. A. M. Kulkarni<br>
            <i>Chemistry faculty at Pune Institute of Computer Technology, Pune</i><br><br>
            <b>A Flask web application by:</b><br><br>
            Advait Joshi<br>
            <i>CE Undergrad at Pune Institute of Computer Technology, Pune</i><br>
            Email: joshiadvait07@gmail.com<br>
            <a href="https://www.linkedin.com/in/advait-joshi-b61410256">Click to view LinkedIn profile</a>

        '''

if __name__ == '__main__':
    app.run(port="5005")