struct Tree {
    root: f64,
    left: Option<Box<Tree>>,
    right: Option<Box<Tree>>,
}

fn is_binary_search_tree(t: &Option<Box<Tree>>, min: f64, max: f64) -> bool {
    match *t {
        Some(ref t) => {
            if min < t.root && t.root < max {
                return is_binary_search_tree(&t.left, min, t.root) &&
                       is_binary_search_tree(&t.right, t.root, max);
            }
            false
        }
        None => true, // An empty tree is a balanced tree :-)
    }
}

fn main() {
    let t0 = Tree {
        root: 1.0,
        left: None,
        right: None,
    };
    assert_eq!(is_binary_search_tree(&Some(Box::new(t0)), -std::f64::INFINITY, std::f64::INFINITY),
               true);

    let t1 = Tree {
        root: 15.0,
        left: Some(Box::new(Tree {
            root: 12.0,
            left: None,
            right: Some(Box::new(Tree {
                root: 13.0,
                left: None,
                right: None,
            })),
        })),
        right: Some(Box::new(Tree {
            root: 22.0,
            left: Some(Box::new(Tree {
                root: 18.0,
                left: None,
                right: None,
            })),
            right: Some(Box::new(Tree {
                root: 100.0,
                left: None,
                right: None,
            })),
        })),
    };
    assert_eq!(true,
               is_binary_search_tree(&Some(Box::new(t1)), -std::f64::INFINITY, std::f64::INFINITY));

    let t2 = Tree {
        root: 15.0,
        left: Some(Box::new(Tree {
            root: 18.0,
            left: None,
            right: None,
        })),
        right: None,
    };

    assert_eq!(false,
               is_binary_search_tree(&Some(Box::new(t2)), -std::f64::INFINITY, std::f64::INFINITY));
}
