from flask import Blueprint, jsonify

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    return jsonify({'Movies': 'Movies list'})