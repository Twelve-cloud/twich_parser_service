"""
conftest.py: File, containing some settings for component tests.
"""


import sys

import pytest
from httpx import AsyncClient

from main import app


sys.path.insert(0, './src')


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='class')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
