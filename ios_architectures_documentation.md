# iOS Architectures Documentation

## Repository: munibsiddiqui/ios-architectures

### Architectures and Patterns

1. **MVC**
   - **Storyboard**: UI - Storyboard, Network - URLSession
   - **SnapKit**: UI - SnapKit, Network - URLSession

2. **MVP**
   - **SnapKit**: UI - SnapKit, Then, Network - URLSession

3. **MVVM**
   - **RxSwift - Storyboard**: UI - Storyboard, RxDatasource, Network - RxURLSession, Unit Tests - RxTest
   - **RxSwift - xcodegen**: UI - Storyboard, RxDatasource, Network - RxURLSession, Unit Tests - RxTest, Xcodegen
   - **RxSwift - tuist**: UI - Storyboard, RxDatasource, Network - RxURLSession, Unit Tests - RxTest, Tuist

4. **Clean Architecture**
   - **MVVM - RxSwift - coredata**: Repository Pattern - CoreData, Unit Tests - RxTest, Nimble

5. **VIPER**
   - **SnapKit**: UI - SnapKit, Then, RxDatasource, Network - Moya, Unit Tests - RxTest

6. **RIBs**
   - **SnapKit**: Package Management - SPM, UI - SnapKit, Then, RxDatasources, Network - Moya, Unit Tests

### Notes
- The repository includes various UI frameworks, networking solutions, and dependency injection frameworks.
- It covers architectures like MVC, MVP, MVVM, VIPER, and RIBs with different implementations.

## Next Steps
- Continue documenting architectural patterns from other repositories.
- Organize the data for model training.
