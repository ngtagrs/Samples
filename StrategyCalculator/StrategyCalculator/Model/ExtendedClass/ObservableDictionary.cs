using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;

public class ObservableDictionary<TKey, TValue> : IDictionary<TKey, TValue>, INotifyCollectionChanged, INotifyPropertyChanged
{
    private readonly Dictionary<TKey, TValue> _dictionary = new Dictionary<TKey, TValue>();

    public event NotifyCollectionChangedEventHandler CollectionChanged;
    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnCollectionChanged(NotifyCollectionChangedEventArgs e)
    {
        CollectionChanged?.Invoke(this, e);
    }

    protected virtual void OnPropertyChanged(string propertyName)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    public void Add(TKey key, TValue value)
    {
        _dictionary.Add(key, value);
        OnCollectionChanged(new NotifyCollectionChangedEventArgs(NotifyCollectionChangedAction.Add, new KeyValuePair<TKey, TValue>(key, value)));
        OnPropertyChanged(nameof(Count));
    }

    public bool Remove(TKey key)
    {
        if (_dictionary.TryGetValue(key, out var value))
        {
            var removedItem = new KeyValuePair<TKey, TValue>(key, value);
            if (_dictionary.Remove(key))
            {
                OnCollectionChanged(new NotifyCollectionChangedEventArgs(NotifyCollectionChangedAction.Remove, removedItem));
                OnPropertyChanged(nameof(Count));
                return true;
            }
        }
        return false;
    }

    // 他の IDictionary<TKey, TValue> メソッドの実装も必要です

    public ICollection<TKey> Keys => _dictionary.Keys;

    public ICollection<TValue> Values => _dictionary.Values;

    public int Count => _dictionary.Count;

    public bool IsReadOnly => ((IDictionary<TKey, TValue>)_dictionary).IsReadOnly;

    public TValue this[TKey key]
    {
        get => _dictionary[key];
        set
        {
            if (_dictionary.TryGetValue(key, out var existingValue))
            {
                _dictionary[key] = value;
                OnCollectionChanged(new NotifyCollectionChangedEventArgs(NotifyCollectionChangedAction.Replace, new KeyValuePair<TKey, TValue>(key, value), new KeyValuePair<TKey, TValue>(key, existingValue)));
                OnPropertyChanged(nameof(Values));
            }
            else
            {
                Add(key, value);
            }
        }
    }

    public bool ContainsKey(TKey key) => _dictionary.ContainsKey(key);

    public bool TryGetValue(TKey key, out TValue value) => _dictionary.TryGetValue(key, out value);

    public void Add(KeyValuePair<TKey, TValue> item) => Add(item.Key, item.Value);

    public void Clear()
    {
        _dictionary.Clear();
        OnCollectionChanged(new NotifyCollectionChangedEventArgs(NotifyCollectionChangedAction.Reset));
        OnPropertyChanged(nameof(Count));
    }

    public bool Contains(KeyValuePair<TKey, TValue> item) => ((IDictionary<TKey, TValue>)_dictionary).Contains(item);

    public void CopyTo(KeyValuePair<TKey, TValue>[] array, int arrayIndex) => ((IDictionary<TKey, TValue>)_dictionary).CopyTo(array, arrayIndex);

    public bool Remove(KeyValuePair<TKey, TValue> item)
    {
        if (Contains(item))
        {
            return Remove(item.Key);
        }
        return false;
    }

    public IEnumerator<KeyValuePair<TKey, TValue>> GetEnumerator() => _dictionary.GetEnumerator();

    IEnumerator IEnumerable.GetEnumerator() => ((IEnumerable)_dictionary).GetEnumerator();
}
