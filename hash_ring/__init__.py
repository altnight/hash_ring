from .ring import HashRing

try:
    from .memcache_ring import MemcacheRing
except ImportError as e:
    pass
