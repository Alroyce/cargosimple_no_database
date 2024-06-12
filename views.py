from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A temporary list to store cargo bookings
cargo_bookings = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book_cargo', methods=['GET', 'POST'])
def book_cargo():
    if request.method == 'POST':
        cargo_details = {
            'sender_name': request.form['sender_name'],
            'sender_address': request.form['sender_address'],
            'receiver_name': request.form['receiver_name'],
            'receiver_address': request.form['receiver_address'],
            'cargo_type': request.form['cargo_type']
        }
        cargo_bookings.append(cargo_details)
        return redirect(url_for('booking_confirmation'))
    return render_template('book_cargo.html')

@app.route('/booking_confirmation')
def booking_confirmation():
    if cargo_bookings:
        latest_booking = cargo_bookings[-1]
        return render_template('booking_confirmation.html', booking=latest_booking)
    else:
        return "No bookings yet!"

if __name__ == '__main__':
    app.run(debug=True)
