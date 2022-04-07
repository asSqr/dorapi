from dataclasses import asdict
from .data_struct import Gadget, Book
from dorapi.models import MGadget, MBook
from dorapi.enums import BookSeriesEnum


def mbook_to_book(mbook: MBook) -> Book:
    book = Book(
        series=BookSeriesEnum(mbook.series),
        volume=mbook.volume,
    )
    
    return book


def book_to_mbook(book: Book) -> MBook:
    book_dict = asdict(book)
    book_dict['series'] = book.series.value
    
    mbook = MBook(**book_dict)
    
    return mbook


def gadget_to_mgadget(gadget: Gadget) -> MGadget:
    gadget_dict = asdict(gadget)
    del gadget_dict['books']
    
    mgadget = MGadget(**gadget_dict)
    
    return mgadget


def mgadget_to_gadget(mgadget: MGadget) -> Gadget:
    gadget = Gadget(
        name=mgadget.name,
        ruby=mgadget.ruby,
        desc=mgadget.desc,
        href=mgadget.href,
        image_url=mgadget.image_url,
        total_results=mgadget.total_results,
        books=map(mbook_to_book, mgadget.mbooks.all()),
    )
    
    return gadget


def generate_gadget_key(gadget: Gadget) -> str:
    return f'{gadget.name}-{gadget.ruby}-{gadget.desc}'


def generate_mgadget_key(mgadget: MGadget) -> str:
    return f'{mgadget.name}-{mgadget.ruby}-{mgadget.desc}'


def generate_book_key(book: Book) -> str:
    return f'{book.series.value}-{book.volume}'


def generate_mbook_key(mbook: MBook) -> str:
    return generate_book_key(mbook_to_book(mbook))
